from app.core.database import Base
from sqlalchemy import Column,String,Integer,Enum,DateTime,Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

class RoleCheck(str,enum.Enum):
    customer="customer",
    fundi="fundi"

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    phone=Column(String,nullable=False,unique=True)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    role=Column(Enum(RoleCheck),default=RoleCheck.customer)
    is_active=Column(Boolean,default=True)
    is_verified=Column(Boolean,default=True)
    
    created_at=Column(DateTime,default=datetime.now())
    updated_at=Column(DateTime,default=datetime.now(),onupdate=datetime.now())
    
    refreshtoken=relationship("RefreshToken",back_populates="user")
    customer=relationship("Customer",back_populates="user",cascade="all,delete-orphan")