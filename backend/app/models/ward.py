from app.core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String,Column,Integer,DateTime,ForeignKey
from datetime import datetime

class Ward(Base):
    __tablename__="wards"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    district_id=Column(Integer,ForeignKey("districts.id"))
    created_at=Column(DateTime,default=datetime.now)
    updated_ay=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    district=relationship("District",back_populates="ward")
    street=relationship("Street",back_populates="ward",cascade="all,delete")
    
    
    