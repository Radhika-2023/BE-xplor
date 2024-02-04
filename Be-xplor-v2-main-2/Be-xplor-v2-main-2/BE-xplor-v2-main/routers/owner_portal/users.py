
from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
from schemas.owner_portal import Users
from fastapi import APIRouter
from database import get_db

# Define API router
router = APIRouter(
    prefix='/user',
    tags=['User']
)

# Endpoint to create a new user
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Users.CreateUser)
def create_user(create_user_request: Users.CreateUser, db: Session = Depends(get_db)):
    new_user = models.Users(**create_user_request.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


