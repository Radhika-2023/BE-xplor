from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, REAL, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

class Organizations(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Locations(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    org_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    latitude = Column(REAL, nullable=False)
    longitude = Column(REAL, nullable=False)
    is_active = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Vehicles(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, nullable=False)
    org_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    reg_no = Column(String, unique=True, index=True)
    driver_user_id = Column(Integer, ForeignKey('users.id'),nullable=False)
    vehicle_capacity = Column(Integer)
    service_type = Column(String)
    # is_active = Column(Boolean, server_default='TRUE')
    # created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    # updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
   

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    contact_number = Column(String)
    type = Column(String)
    org_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    # is_active = Column(Boolean, server_default='TRUE')
    # created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    # updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Vehicle_route_mapping(Base):
    __tablename__ = "vehicle_route_mapping"

    id = Column(Integer, primary_key=True, nullable=False)  
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    route_id = Column(Integer, ForeignKey('routes.id'), nullable=False)
    # is_active = Column(Boolean, server_default='TRUE')
    # created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    # updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


class vehicle_route_schedule(Base):
    __tablename__ = "vehicle_route_schedule"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    #route_id = Column(Integer, ForeignKey('routes.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))
    location_time = Column(DateTime)

class Routes(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(Integer, ForeignKey('organizations.id'),nullable=False)
    created_by = Column(Integer, ForeignKey('users.id'),nullable=False)
    ticket_prices = Column(Float)

# insert into organizations(id, name) values (0, 'Default Org');
# insert into locations(name, org_id, latitude, longitude)
# values('Kochi Airport', 1, 3.34534345, 5.5745645);
    

# SELECT Vehicles.VehiclesID, Vehicles.org_id, Vehicles.reg_no,Vehicles.driver_user_id,Vehicles.vehicle_capacity,
# Routes.Routesid,Routes.Routesorg_id,
# FROM Vehicles
# JOIN Routes ON Vehicles.RoutesID = Routes.RoutesID;
    

# SELECT v.id AS vehicle_id, v.reg_no, u.id AS user_id, u.username
# FROM vehicles v
# JOIN users u ON v.driver_user_id = u.id;
