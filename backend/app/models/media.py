from app.core.database import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class MediaCustomer(Base):
    __tablename__="media"
    
    id=Column(Integer,primary_key=True)
    path=Column(String)
    filename=Column(String)
    new_filename=Column(String)
    uploaded_by=Column(Integer,ForeignKey("customers.id"))
    uploaded_at=Column(DateTime,default=datetime.now())
    
    customer_uploadedby=relationship("Customer",foreign_keys=[uploaded_by],back_populates="media")
    customer_picture=relationship("Customer",foreign_keys="Customer.profile_picture",back_populates="picture")