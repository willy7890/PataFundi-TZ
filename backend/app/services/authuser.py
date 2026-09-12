from app.schemas.user import CreateUser,UserUpdate
from app.models.user import User
from sqlalchemy.orm import Session
from app.models.refreshtoken import RefreshToken,Revoked
from app.core.security import hash_password,verify_password,create_access_token,create_refresh_token,decode_token
from fastapi import HTTPException,status,Depends
from datetime import datetime,timedelta


class UserServices():
    @staticmethod
    def register_user(data:CreateUser,db:Session):
        existing=db.query(User).filter(User.email==data.email).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail="email alreaady exist")
        phone=db.query(User).filter(User.phone==data.phone).first()
        if phone:
            raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail="phone already exist")
        user=User(
            phone=data.phone,
            email=data.email,
            role=data.role,
            password=hash_password(data.password)
            
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return user
    
    @staticmethod
    def login(email:str,password:str,db:Session):
        user=db.query(User).filter(User.email==email).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="wrong email")
        if not verify_password(password,user.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="wrong password")
        token=create_access_token({"sub":user.email})
        
        refresh_token_str=create_refresh_token()
        
        stored=db.query(RefreshToken).filter(
            RefreshToken.id==user.id,
            RefreshToken.revoked==False
        ).first() 
        if stored:
            stored.token=refresh_token_str,
            expired_at=datetime.now() +timedelta(days=2)
            db.commit()
            db.refresh(stored)
            
        else:
            refresh_token=RefreshToken(
                user_id=user.id,
                token=refresh_token_str,
                expired_at=datetime.now() +timedelta(days=2),
                revoked=False
            
            )            
            db.add(refresh_token)
            db.commit()
            db.refresh(refresh_token)            
            

        return{
            "access_token":token,
            "refresh_token":refresh_token_str,
            "token_type":"Bearer"
        }
        
    @staticmethod
    def refresh_token(refreshtoken:str,db:Session):
        stored=db.query(RefreshToken).filter(
            RefreshToken.token==refreshtoken,
            RefreshToken.revoked==False
        ).first()
        if not stored:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid refresh token")
        if stored.expired_at < datetime.now():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="expired refresh token")
        user=db.query(User).filter(User.id==stored.id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
        new_access_token=create_access_token({"sub":user.email})
        
        return{
            "access_token":new_access_token,
            "token_type":"Bearer"
        }
        
    @staticmethod
    def logout(current_user,db:Session,
               access_token:str,refresh_token:str):
        refresh=db.query(RefreshToken).filter(
            RefreshToken.user_id==current_user.id,
            RefreshToken.token==refresh_token,
            RefreshToken.revoked==False
            ).first()

        if not refresh:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid refresh token")
        if refresh.expired_at < datetime.now():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="expired refresh token") 
        refresh.revoked=True
        db.commit()
        db.refresh(refresh)      
        
          
        payload=decode_token(access_token)
        revoked=Revoked(
            token=access_token,
            expire_at=datetime.fromtimestamp(payload["exp"])
        )
        db.add(revoked) 
        db.commit()  
        db.refresh(revoked)
        
        return {
            "message":"logout succesful",
            "revoked":revoked
        }
        
    @staticmethod
    def all_user(db:Session):
        user=db.query(User).all()    
        return user
    
    @staticmethod
    def update(data:UserUpdate,db:Session,current_user):
        user=db.query(User).filter(User.id==current_user.id).first()
        if data.email:
            user.email=data.email
        if data.phone:
            user.phone=data.phone
        if data.role:
            user.role=data.role
            
        db.commit()        
        db.refresh(user)
        
        return user
    
    @staticmethod
    def changePassword(old_password:str,new_password:str,db:Session,current_user):
        user=db.query(User).filter(User.id==current_user.id).first()
        if old_password==new_password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="password might not the same")        
        
        if not verify_password(old_password,user.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="wrong old password")

        user.password==hash_password(new_password)
        db.commit()
        db.refresh(user)
        
        return {
            "message":"password is succesfuly updated"
        }
        
    