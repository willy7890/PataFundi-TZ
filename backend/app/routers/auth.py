from fastapi import APIRouter
from app.schemas.user import CreateUser,UserUpdate,UserResponse
from fastapi import Depends
from app.core.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.services.authuser import UserServices
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import CreateUser,UserResponse,UserUpdate
from app.models.user import User
from app.core.security import get_current_user
from fastapi.security import OAuth2PasswordBearer

oauth2_schema=OAuth2PasswordBearer(tokenUrl="/login")

router=APIRouter(tags=["Auth"])


@router.post("/register",response_model=UserResponse)
def register(data:CreateUser,db:Session=Depends(get_db)):
    return  UserServices.register_user(data,db)

@router.post("/login")
def login(data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    return UserServices.login(data.username,data.password,db)

@router.post("/tokenrefresh")
def refresh(refreshtoken:str,db:Session=Depends(get_db)):
    return UserServices.refresh_token(refreshtoken,db)


@router.post("/logout")
def logout( refresh_token:str,current_user:User=Depends(get_current_user),
           db:Session=Depends(get_db),
           token:str=Depends(oauth2_schema)):
    return UserServices.logout(current_user,db=db,access_token=token,refresh_token=refresh_token)
