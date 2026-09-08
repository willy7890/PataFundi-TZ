from sqlalchemy.orm import Session
from app.models.regions import Region
from app.models.district import District
from app.models.ward import Ward
from app.models.street import Street
from fastapi import Query,HTTPException,status
from sqlalchemy import or_,desc,asc
import math


class region_Sesrvice():
    @staticmethod
    def regionlist(db:Session,
                   search:str=None,page:int=Query(1,ge=1),
                   limit:int=Query(10 ,ge=10,le=100),sort:str=None,oder:str="desc"):
        region=db.query(Region)
        
        if search:
            region=region.filter(or_(
                Region.name.ilike(f"%{search}%"),
                Region.code.ilike(f"%{search}%")
            ))
        
        if sort:
            if sort=="name":
                region=region.order_by(asc(Region.name))   
            else:
                region=region.order_by(desc(Region.name))
        else:
            if sort=="created_at":
                region=region.order_by(asc(Region.created_at))
            else:
                region=region.order_by(desc(Region.created_at))
    
        skip=(page-1)*limit
        total=region.count()   
        total_pages=math.ceil(total/limit)
        
        region=region.offset(skip).limit(limit).all()
        
        return {
            "page":page,
            "total_regions":total,
            "total_pages":total_pages,
            "region":region
        }
        
    @staticmethod
    def region(region_id:int,db:Session):
        region=db.query(Region).filter(Region.id==region_id).first()    
        if not region:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"region with id {region_id} not found @All")
        return region
    
