from sqlalchemy.orm import Session
from app.models.regions import Region
from app.models.district import District
from app.models.ward import Ward
from app.models.street import Street
from fastapi import Query,HTTPException,status
from sqlalchemy import or_,desc,asc
import math


class Street_Service():
    
    @staticmethod
    def list_street(db:Session,search:str=None,page:int=Query(1,ge=1),
                      limit:int=Query(50,le=100,ge= 50),
                      sort:str=None,oder:str="desc"):
        Street=db.query(Street)
        
        if search:
            street=street.filter(
                Street.name.ilike(f"%{search}%")
            )
        if sort:
            if sort=="name":
                street=street.order_by(asc(Street.name))
            else:
                street=street.order_by(desc(street.name))
        else:
            if sort=="created_at":
                street=street.order_by(asc(street.created_at))
                street=street.order_by(desc(Street.created_at))
         
        skip=(page-1)*limit
        total=Street.count()       
        total_pages=math.ceil(total/limit)
        
        street=street.offset(skip).limit(limit).all()
        
        return{
            "page":page,
            "total_regions":total,
            "total_pages":total_pages,
            "streets":street
        }                        
            
        
    @staticmethod
    def single_street(street_id:int,db:Session):
        street=db.query(Street).filter(Ward.id==street_id).first()    
        if not street:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"street wth id {street_id} not found")
        return street
    
    @staticmethod
    def street_ward(street_id:int,db:Session):
        ward=db.query(Street).filter(Street.id==street_id).first()
        if not ward:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="street not found")
        street=db.query(Street).filter(Street.ward_id==ward.id).all()
        if not street:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no streetfound @all")
        return{
            "total":len(street),
            "ward":street
        }
            