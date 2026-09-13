from pydantic import BaseModel,EmailStr,ConfigDict,field_validator,Field
from app.models.user import RoleCheck
from typing import Optional
from datetime import datetime

class CreateUser(BaseModel):
    phone:str="+225618982523"
    email:EmailStr
    password:str
    role:RoleCheck
    
   
    
class UserUpdate(BaseModel):
    phone:Optional[str]=None
    email:Optional[EmailStr]=None
    password:Optional[str]=None
    role:Optional[RoleCheck]=None
    
    model_config=ConfigDict(
        from_attributes=True
    )    
class UserResponse(BaseModel):
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
    