from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class CustomerProfileCreate(BaseModel):
    full_name:str
    gender:Optional[str]=None
    date_of_birth:Optional[date]=None
    bio:Optional[str]=None

class CustomerProfileUpdate(BaseModel):
    full_name:Optional[str]=None
    gender:Optional[str]=None
    date_of_birth:Optional[date]=None
    bio:Optional[str]=None

class CustomerProfileResponse(BaseModel):
    id:int
    full_name:str
    user_id:int
    gender:Optional[str]=None
    date_of_birth:Optional[date]=None
    age:Optional[int]=None
    profile_picture:Optional[int]=None
    bio:Optional[str]=None
    created_at:datetime
    updated_at:datetime  
    