from pydantic import BaseModel
from datetime import datetime
from typing import Union

# ------------------------------------ Organizations ------------------------------------

class OrganizationsBase(BaseModel):
    id: Union[int, None] = None
    name: str
    is_active: Union[bool, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None

    class Config:
        orm_mode = True


class CreateOrganization(OrganizationsBase):
    class Config:
        orm_mode = True


class CreateOrganizationsRequest(BaseModel):
    name: str
