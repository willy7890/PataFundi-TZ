from app.core.database import Base
from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class District(Base):
    __tablename__="districts"
    
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    region_id=Column(Integer,ForeignKey("regions.id"))
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    region=relationship("Region",back_populates="district")
    ward=relationship("Ward",back_populates="district",cascade="all , delete-orphan")
    