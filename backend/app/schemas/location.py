from pydantic import BaseModel,ConfigDict
from datetime import datetime


class RegionResponse(BaseModel):
    id:int
    name:str
    
    model_config=ConfigDict(
        from_attributes=True
    )
        
class DistrictResponse(BaseModel):
    id:int
    name:str
    region_id:int
    created_at:datetime
    updated_at:datetime

class WardResponse(BaseModel):
    id:int
    name:str
    district_id:int
 
    
class StreetResponse(BaseModel):
    id:int
    name:str
    ward_id:int