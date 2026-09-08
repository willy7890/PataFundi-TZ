from fastapi import APIRouter,Query,Depends
from app.services.region import region_Sesrvice
from sqlalchemy.orm import Session
from app.core.database import get_db
from typing import List
from app.schemas.location import RegionResponse,DistrictResponse

router=APIRouter(prefix="/location",tags=["Region Location"])

@router.get("/region")
def regions(db:Session=Depends(get_db),search:str=None,page:int=Query(1, ge=1),
            limit:int=Query(10,ge=10,le=100),sort:str=None,oder:str="desc"):
    return region_Sesrvice.regionlist(db,search,page,limit,sort,oder)

@router.get("/region/{region_id}")
def singleregion(region_id:int,db:Session=Depends(get_db)):
    return region_Sesrvice.region(region_id,db)
