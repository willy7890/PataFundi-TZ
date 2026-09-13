from fastapi import APIRouter
from app.schemas.user import UserUpdate,UserResponse
from fastapi import Depends
from app.core.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.services.authuser import UserServices
from app.schemas.user import UserResponse,UserUpdate
from app.models.user import User
from app.core.security import get_current_user


router=APIRouter(prefix="/user",tags=["User"])


@router.get("/me",response_model=UserResponse)
def myinfo(current_user:User=Depends(get_current_user)):
    return current_user

@router.get("/all_user",response_model=List[UserResponse])
def all_user(db:Session=Depends(get_db)):
    return UserServices.all_user(db)

@router.put("/me")
def update_myaccount(data:UserUpdate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return UserServices.update(data,db,current_user)

@router.put("/password")
def change_password(old_password:str,new_password:str,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return UserServices.changePasswor(old_password,new_password,db,current_user)
    