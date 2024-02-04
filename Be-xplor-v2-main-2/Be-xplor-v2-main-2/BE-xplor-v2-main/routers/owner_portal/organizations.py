from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
from schemas.owner_portal import Organizations  
from fastapi import APIRouter
from database import get_db

from pydantic import BaseModel
from datetime import datetime

router = APIRouter(
    prefix='/organization',
    tags=['Organization']
)

# -- 1. Create New Organization  
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Organizations.CreateOrganization)  
def create_organization(create_organization_request: Organizations.CreateOrganization, db: Session = Depends(get_db)):
    new_organization = models.Organizations(**create_organization_request.dict())  
    db.add(new_organization)
    db.commit()
    db.refresh(new_organization)
    return new_organization  
