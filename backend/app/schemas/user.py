from pydantic import BaseModel,EmailStr,ConfigDict,field_validator,Field
from app.models.user import RoleCheck
from typing import Optional
from datetime import datetime
import re

class CreateUser(BaseModel):
    phone:str="+225618982523"
    email:EmailStr
    password:str
    role:RoleCheck
    
    @field_validator("phone")
    @staticmethod
    def phone(cls,value):
        if  not len(value) == 13:
            raise ValueError("phone must have 13 number")
        if not value.startswith("+225"):
            raise ValueError("phone must stat with +225......")
        return value
            
        
    @field_validator("password")
    @staticmethod
    def pwd(cls,value):
        if len(value) < 8:
            raise ValueError("password must have at least 8 character")
        if not re.search(r"[0-9]",value):
            raise ValueError("password must contain atleat one integer")
        if not re.search(r"[A-Z]",value):
            raise ValueError("password must contain atleat one capital leter")
        return value
            
    
   
        
    
class UserUpdate(BaseModel):
    phone:Optional[str]=None
    email:Optional[EmailStr]=None
    password:Optional[str]=None
    role:Optional[RoleCheck]=None
    
    model_config=ConfigDict(
        from_attributes=True
    )    
class UsetResponse(BaseModel):
    id:int
    phone:str
    email:EmailStr
    role:RoleCheck
    is_active:bool
    is_verified:bool
    created_at:datetime
    updated_at:datetime

    model_config=ConfigDict(
        from_attributes=True
    )    
    