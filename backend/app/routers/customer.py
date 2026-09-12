from fastapi import APIRouter,Depends,File,UploadFile
from app.schemas.customer import CustomerProfileCreate,CustomerProfileUpdate,CustomerProfileResponse
from app.services.customer import CustomerServices
from app.models.user import User
from typing import List
from app.models.customer import Customer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user

router=APIRouter(prefix="/customer")


@router.post("",response_model=CustomerProfileResponse,tags=["Customer"])
def create(data:CustomerProfileCreate,
           current_user:User=Depends(get_current_user),
           db:Session=Depends(get_db)):
    return CustomerServices.customer_create(data,current_user,db)

@router.get("/all_customer",response_model=List[CustomerProfileResponse],tags=["Customer"])
def customers(db:Session=Depends(get_db)):
       return CustomerServices.all_customer(db)

@router.get("/me",response_model=CustomerProfileResponse,tags=["Customer"])
def get_my(current_user:User=Depends(get_current_user),
           db:Session=Depends(get_db)):
    return CustomerServices.myProfile(current_user,db)

@router.get("/{customt_id}",response_model=CustomerProfileResponse,tags=["Customer"])
def get_single(customer_id:int,current_user:User=Depends(get_current_user),
           db:Session=Depends(get_db)):
    return CustomerServices.get_single(customer_id,db)


@router.put("/customer_id",response_model=CustomerProfileResponse,tags=["Customer"])
def update(customer_id:int,data:CustomerProfileUpdate,
           current_user:User=Depends(get_current_user),
           db:Session=Depends(get_db)):
    return CustomerServices.update_customer(customer_id,data,current_user,db)


@router.delete("/customer_id",tags=["Customer"])
def delete(customer_id:int,db:Session=Depends(get_db),
              current_user:User=Depends(get_current_user)):
       return CustomerServices.deleteme(customer_id,db,current_user)


@router.post("/uploads/customer_id",tags=["Customer Picture"])
async def upload(customer_id:int,db:Session=Depends(get_db),
           file:UploadFile=File(...),
           current_user:User=Depends(get_current_user)):
        
       return await CustomerServices.uploadpicture(customer_id,db,current_user,file)


@router.get("/show/me",tags=["Customer Picture"])
def show(db:Session=Depends(get_db),
           current_user:Customer=Depends(get_current_user)):
       return CustomerServices.get_mypicture(db,current_user)

@router.delete("/delete/me",tags=["Customer Picture"])
def delete(db:Session=Depends(get_db),
           current_user:Customer=Depends(get_current_user)):
       return CustomerServices.deletepicture(db,current_user)


