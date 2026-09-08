from fastapi import APIRouter,Query,Depends
from app.services.ward import Ward_Service
from sqlalchemy.orm import Session
from app.core.database import get_db
from typing import List
from app.schemas.location import RegionResponse,DistrictResponse

router=APIRouter(prefix="/location",tags=["Ward Location"])

@router.get("/ward")
def list_ward(db:Session=Depends(get_db),search:str=None,page:int=Query(1, ge=1),
            limit:int=Query(10,ge=10,le=100),sort:str=None,oder:str="desc"):
    return Ward_Service.ward_list(db,search,page,limit,sort,oder)

@router.get("ward/{ward_id}")
def sigle_ward(ward_id:int,db:Session=Depends(get_db)):
    return Ward_Service.single_ward(ward_id,db)

@router.get("/ward_district/{district_id}")
def ward_district(district_id:int,db:Session=Depends(get_db)):
    return Ward_Service.ward_district(district_id,db)

     