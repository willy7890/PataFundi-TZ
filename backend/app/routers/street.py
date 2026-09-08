from fastapi import APIRouter,Query,Depends
from app.services.street import Street_Service
from sqlalchemy.orm import Session
from app.core.database import get_db
from typing import List
from app.schemas.location import RegionResponse,DistrictResponse

router=APIRouter(prefix="/location",tags=["Street Location"])

@router.get("/street")
def list_street(db:Session=Depends(get_db),search:str=None,page:int=Query(1, ge=1),
            limit:int=Query(10,ge=10,le=100),sort:str=None,oder:str="desc"):
    return Street_Service.list_street(db,search,page,limit,sort,oder)

@router.get("/street/{street_id}")
def sigle_street(street_id:int,db:Session=Depends(get_db)):
    return Street_Service.single_street(street_id,db)

@router.get("/street_ward/{ward_id}")
def street_ward(ward_id:int,db:Session=Depends(get_db)):
    return Street_Service.street_ward(ward_id,db)
          
