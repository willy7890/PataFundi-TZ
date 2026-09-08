from app.core.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship


class Street(Base):
    __tablename__="streets"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    ward_id=Column(Integer,ForeignKey("wards.id"))
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    
    ward=relationship("Ward",back_populates="street")