import datetime
from typing import Union

from pydantic import BaseModel
from datetime import datetime


# ------------------------------------ Vehicles ------------------------------------
class VehiclesBase(BaseModel):
    id: Union[int, None] = None
    org_id: int
    reg_no: str
    driver_user_id: int
    vehicle_capacity: int
    service_type:str
    # is_active: Union[bool, None] = None
    # created_at: Union[datetime, None] = None
    # updated_at: Union[datetime, None] = None


    class Config:
        orm_mode = True


class CreateVehicle(VehiclesBase):
    class Config:
        orm_mode = True


class CreateVehicleRequest(BaseModel):
    org_id: int
    reg_no: str
    driver_user_id: int
    vehicle_capacity: int
    service_type:str