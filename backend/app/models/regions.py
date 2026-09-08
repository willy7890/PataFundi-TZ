from app.core.database import Base
from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Region(Base):
    __tablename__="regions"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    code=Column(String,nullable=False)
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    district=relationship("District",back_populates="region",cascade="all, delete-orphan")