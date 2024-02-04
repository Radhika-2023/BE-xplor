from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
from schemas.owner_portal import Vehicle_route_mapping 
from fastapi import APIRouter
from database import get_db

from pydantic import BaseModel
from datetime import datetime

router = APIRouter(
    prefix='/vehicle_route_mapping',
    tags=['Vehicle_route_mapping']
)

# -- 1. Create New Organization  
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Vehicle_route_mapping.CreateVehicle_route_mapping)  
def create_vehicle_route_mapping(create_vehicle_route_mapping_request: Vehicle_route_mapping.CreateVehicle_route_mapping, db: Session = Depends(get_db)):
    new_vehicle_route_mapping = models.Vehicle_route_mapping(**create_vehicle_route_mapping_request.dict())  
    db.add(new_vehicle_route_mapping)
    db.commit()
    db.refresh(new_vehicle_route_mapping)
    return new_vehicle_route_mapping  
