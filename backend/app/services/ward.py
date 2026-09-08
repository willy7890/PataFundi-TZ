from sqlalchemy.orm import Session
from app.models.regions import Region
from app.models.district import District
from app.models.ward import Ward
from app.models.street import Street
from fastapi import Query,HTTPException,status
from sqlalchemy import or_,desc,asc
import math


class Ward_Service():
    
    @staticmethod
    def ward_list(db:Session,search:str=None,
                  page:int=Query(1,ge=1),limit:int=Query(100,ge=100,le=500),
                  sort:str=None,oder:str="desc"):
        ward=db.query(Ward)
        
        if search:
            ward=ward.filter(
                Ward.name.ilike(f"%{search}")
            )
        if sort:
            if sort=="name":
                ward=ward.order_by(asc(Ward.name))    
            else:
                ward=ward.order_by(desc(Ward.name))
        else:
            if sort=="created_at":
                ward=ward.order_by(asc(Ward.created_at))                        
            else:
                ward=ward.order_by(desc(Ward.created_at))
                
        skip=(page-1)*limit
        total=ward.count()
        total_pages=math.ceil(total/limit)   
        ward=ward.offset(skip).limit(limit).all()
        return {
            "page":page,
            "total":total,
            "total_pages":total_pages,
            "ward":ward    
        }    

    @staticmethod
    def single_ward(ward_id:int,db:Session):
        ward=db.query(Ward).filter(Ward.id==ward_id).first()    
        if not ward:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"ward wth id {ward_id} not found")
        return ward
    
    @staticmethod
    def ward_district(district_id:int,db:Session):
        district=db.query(District).filter(District.id==district_id).first()
        if not district:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="district not found")
        ward=db.query(Ward).filter(Ward.district_id==district.id).all()
        if not ward:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no ward found @all")
        return{
            "total":len(ward),
            "ward":ward
        }
        
    