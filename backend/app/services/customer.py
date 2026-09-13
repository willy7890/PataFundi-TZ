from app.schemas.customer import CustomerProfileCreate,CustomerProfileUpdate
from app.models.customer import Customer
from sqlalchemy.orm import Session
from app.models.user import RoleCheck
from fastapi import HTTPException,status,File,UploadFile
from pathlib import Path
from datetime import date
from uuid import uuid4
from app.models.media import MediaCustomer

class CustomerServices():
    
    @staticmethod
    def calculate_age(dob:date):
        today=date.today()
        if dob.year > today.year:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="date of birth cnnot br in ffuture")
        age=today.year-dob.year-((today.month,today.day)<(dob.month,dob.day))
        return age
        
    @staticmethod
    def customer_create(data:CustomerProfileCreate,current_user,db:Session):
        customer=db.query(Customer).filter(Customer.user_id==current_user.id).first()
        if customer:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="customer already have an account")
    
        if current_user.role != RoleCheck.customer:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="only authorized registerd customer can access")
        customer=Customer(
            full_name=data.full_name,
            gender=data.gender,
            date_of_birth=data.date_of_birth,
            user_id=current_user.id,
            bio=data.bio,
            age=CustomerServices.calculate_age(data.date_of_birth)
        )
        db.add(customer)
        db.commit()
        db.refresh(customer)
    
        return customer

    @staticmethod
    def all_customer(db:Session):
        customer=db.query(Customer).all()
        return customer
    
    @staticmethod
    def myProfile(current_user,db:Session):
        customer=db.query(Customer).filter(Customer.user_id==current_user.id).first()
        if not customer:
            return None
        return customer
    
    @staticmethod
    def get_single(customer_id:int,db:Session):
        customer=db.query(Customer).filter(Customer.id==customer_id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="customer not found")
        return customer
    
    @staticmethod
    def update_customer(customer_id:int,data:CustomerProfileUpdate,current_user,db:Session):
        customer=db.query(Customer).filter(Customer.id==customer_id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="customer not found at all")
        if customer.user_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="customer not found")
        if data.full_name:
            customer.full_name=data.full_name
        if data.gender:    
            customer.gender=data.gender
        if data.date_of_birth:    
            customer.date_of_birth=data.date_of_birth
            customer.age=CustomerServices.calculate_age(data.date_of_birth)
        if data.bio:    
            customer.bio=data.bio
    
        db.commit()
        db.refresh(customer)
        return customer
    
    @staticmethod
    def deleteme(customer_id:int,db:Session,current_user):
        customer=db.query(Customer).filter(Customer.id==customer_id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ucustomer not found at all")
        if customer.user_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="customer not found")        
        user=customer.user
        db.delete(customer)
        db.delete(user)
        db.commit()
        return{
            "message":"deleted successfuly"
        }
    
    @staticmethod
    async def uploadpicture(customer_id:int,db:Session,current_user,file:UploadFile=File(...)):
        
        customer=db.query(Customer).filter(Customer.id==customer_id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="customer not found")
        if customer.user_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="you not have action to perfom this")
        UPLOAD_DIR=Path("storage/uploads/image")
        UPLOAD_DIR.mkdir(parents=True,exist_ok=True)
        
        ALLOWED_EXTENSION=(
            ".png",".peg",".jpg"
        )
        if not file.content_type:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="file has no content")
        
        extension=Path(file.filename).suffix.lower()
        if extension not in ALLOWED_EXTENSION:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="file type not allowed")
        
        new_filename=f"customer_{uuid4()}-{extension}"
        file_path=(UPLOAD_DIR/new_filename)
        
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        
        media=db.query(MediaCustomer).filter(MediaCustomer.id==customer.profile_picture).first()
        if media:
            media.filename=file.filename
            media.new_filename=new_filename
            media.path=str(file_path)
        else:
            media=MediaCustomer(
                filename=file.filename,
                new_filename=new_filename,
                path=str(file_path),
                uploaded_by=customer.id
            )
            db.add(media)
            db.flush()
            customer.profile_picture=media.id
        db.commit()    
        db.refresh(media)
        
        return media
    @staticmethod
    def get_mypicture(db:Session,current_user):
        customer=db.query(Customer).filter(Customer.user_id==current_user.id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="access denied")
        media=db.query(MediaCustomer).filter(MediaCustomer.id==customer.profile_picture).first()
        if not media:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="you dont have profile picture")
        return media
    
    @staticmethod
    def deletepicture(db:Session,current_user):
        customer=db.query(Customer).filter(Customer.user_id==current_user.id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="access denied")
        media=db.query(MediaCustomer).filter(MediaCustomer.id==customer.profile_picture).first()
        if not media:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="you dont have profile picture")
        db.delete(media)
        db.commit()
        return {
            "message":"profile picture successful removed"
        }
            
    
      
            
            