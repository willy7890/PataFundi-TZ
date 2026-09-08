from fastapi import APIRouter,Query,Depends
from app.services.district import District_services
from sqlalchemy.orm import Session
from app.core.database import get_db
from typing import List
from app.schemas.location import RegionResponse,DistrictResponse

router=APIRouter(prefix="/location",tags=[" District Location"])

@router.get("/district")
def list_district(db:Session=Depends(get_db),
                  search:str=None,page:int=Query(1,ge=1),
                limit:int=Query(50,le=100,ge= 50),sort:str=None,oder:str="desc"):
    return District_services.list_district(db,search,page,limit,sort,oder)

@router.get("district/{district_id}",response_model=DistrictResponse)
def district(district_id:int,db:Session=Depends(get_db)):
    return District_services.single_district(district_id,db)

@router.get("/district_region/{region_id}")
def district_region(region_id:int,db:Session=Depends(get_db)):
    return District_services.district_region(region_id,db)
       

