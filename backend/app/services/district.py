from sqlalchemy.orm import Session
from app.models.regions import Region
from app.models.district import District
from app.models.ward import Ward
from app.models.street import Street
from fastapi import Query,HTTPException,status
from sqlalchemy import or_,desc,asc
import math


class District_services():
    @staticmethod
    def list_district(db:Session,search:str=None,page:int=Query(1,ge=1),
                      limit:int=Query(50,le=100,ge= 50),
                      sort:str=None,oder:str="desc"):
        district=db.query(District)
        
        if search:
            district=district.filter(
                District.name.ilike(f"%{search}%")
            )
        if sort:
            if sort=="name":
                district=district.order_by(asc(District.name))
            else:
                district=district.order_by(desc(District.name))
        else:
            if sort=="created_at":
                district=district.order_by(asc(District.created_at))
                district=district.order_by(desc(District.created_at))
         
        skip=(page-1)*limit
        total=district.count()       
        total_pages=math.ceil(total/limit)
        
        district=district.offset(skip).limit(limit).all()
        
        return{
            "page":page,
            "total_regions":total,
            "total_pages":total_pages,
            "district":district
        } 
        
    @staticmethod
    def single_district(district_id:int,db:Session):
        district=db.query(District).filter(District.id==district_id).first()
        if not district:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")
        return district
    
    @staticmethod
    def district_region(region_id:int,db:Session):
        region=db.query(Region).filter(Region.id==region_id).first()
        if not region:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="region not found")
        district=db.query(District).filter(District.region_id==region_id).all()
        
        if not district:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="sorry the region`s district not found")
        total=len(district)
        return {
            "total":total,
            "district":district
        }
                                       
                
    
    
    
    