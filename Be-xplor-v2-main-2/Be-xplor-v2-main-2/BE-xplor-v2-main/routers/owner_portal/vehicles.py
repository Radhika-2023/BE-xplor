from sqlite3 import IntegrityError

from typing import List
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
from schemas.owner_portal import Vehicles
from fastapi import APIRouter
from database import get_db

from pydantic import BaseModel
from datetime import datetime

router = APIRouter(
    prefix='/erp/vehicle',
    tags=['Vehicle']
)

# -- 1. Create New vehicle
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[Vehicles.CreateVehicle])
def create_vehicle(create_vehicle_request:Vehicles.CreateVehicle, db: Session = Depends(get_db)):
    new_vehicle = models.Vehicles(**create_vehicle_request.model_dump())
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return [new_vehicle]



# @router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[Vehicles.CreateVehicle])
# def create_vehicle(request: Vehicles.CreateVehicleRequest, db: Session = Depends(get_db)):
#     new_vehicle = models.vehicles(**request.dict())
#     try:
#         db.add(new_vehicle)
#         db.commit()
#         db.refresh(new_vehicle)
#     except IntegrityError as e:
#         db.rollback()
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Foreign key constraint violation")
#     return [new_vehicle]



# -- 2. Edit vehicles
# 
@router.put('/{request_id}', response_model=Vehicles.CreateVehicle)
def update_vehicle(update_vehicle_req: Vehicles.VehiclesBase, request_id: int, db: Session = Depends(get_db)):
    existing_vehicle = db.query(models.Vehicles).filter(models.Vehicles.id == request_id).first()

    if existing_vehicle is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{request_id} does not exist")
    
    # Update vehicle attributes
    db.query(models.Vehicles).filter(models.Vehicles.id == request_id).update(update_vehicle_req.dict(), synchronize_session=False)
    db.commit()
    
    # Fetch and return the updated vehicle instance
    updated_vehicle = db.query(models.Vehicles).filter(models.Vehicles.id == request_id).first()
    return updated_vehicle




# -- 3. Delete vehicles
@router.delete('/{request_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_vehicle(request_id: int, db: Session = Depends(get_db)):
    deleted_vehicle = db.query(models.Vehicles).filter(models.Vehicles.id == request_id)
    if deleted_vehicle.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {request_id} you requested for does not exist")
    deleted_vehicle.delete(synchronize_session=False)
    db.commit()


# -- 4. Get Single vehicles
# @router.get('/{request_id}', response_model=VehicleRouteResponse, status_code=status.HTTP_200_OK)
# def get_one_vehicle(request_id: int, db: Session = Depends(get_db)):
#     db_entry = db.query(models.Routes).join(models.Vehicles).filter(models.Vehicles.id == request_id).first()

#     if db_entry is None:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                             detail=f"The id: {request_id} you requested for does not exist")
#     return db_entry

@router.get('/{request_id}', response_model=Vehicles.CreateVehicle, status_code=status.HTTP_200_OK)
def get_one_vehicle(request_id: int, db: Session = Depends(get_db)):
    return db.query(models.Vehicles,models.Routes).join(models.Routes).all()
    
    
    # db_entry = db.query(models.Vehicles).filter(models.Vehicles.id == request_id).first()

    # if db_entry is None:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
    #                         detail=f"The id: {request_id} you requested for does not exist")
    # return db_entry


# -- 5. Get all vehicles
@router.get('/', response_model=List[Vehicles.VehiclesBase])
def get_all_vehicles(db: Session = Depends(get_db)):
    return db.query(models.Vehicles).all()








