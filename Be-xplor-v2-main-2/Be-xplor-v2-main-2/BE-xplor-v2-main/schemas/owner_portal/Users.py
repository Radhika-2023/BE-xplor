from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# UserBase schema defines the common fields shared by all users
class UsersBase(BaseModel):
    id: Optional[int] = None
    name: str
    contact_number: str
    type: str
    org_id: int
    # is_active: Optional[bool] = None
    # created_at: Optional[datetime] = None
    # updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

# CreateUser schema inherits from UserBase and adds no additional fields
class CreateUser(UsersBase):
    #pass
    class Config:
        orm_mode = True

# CreateUserRequest schema is used for request bodies in API endpoints
class CreateUserRequest(BaseModel):
    name: str
    contact_number: str
    type: str
    org_id: int
