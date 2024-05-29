from pydantic import BaseModel
from datetime import datetime, timedelta
from database import Base,engine
from sqlalchemy import Column,Integer,String,Boolean,DateTime
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from database import SessionLocal

privatekey="ff247f0ca36ce14dc184314e2e0d6ea6196b22e5fc7491ed2fcd6b668079f2ab"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




class User(Base):

    __tablename__ = "User"    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(250), unique=True, nullable=False)
    email_id = Column(String(250), unique=True, nullable=True)
    password = Column(String(500), nullable=False) 
    is_admin= Column(Boolean,default=False)
    is_staff = Column(Boolean, default=True)
    
    def __init__(self,username:str,password:str,email_id:str):
        self.username=username
        self.password=password
        self.email_id=email_id        
        self.normalize_emailid()
        self.get_password_hash()

    def get_password_hash(self):
        self.password= pwd_context.hash(self.password)
        
    def get_password_verify(self,unhashedpassword :str) ->bool:
        return pwd_context.verify(unhashedpassword,self.password)
    
    def displayuser(self)->dict:
        return {"id":self.id,"username":self.username,"email id":self.email_id,"is staff":self.is_staff,"is admin":self.is_admin}
        
    def insertdata(self):
        with SessionLocal() as db:
            if not db.query(User).filter(User.email_id==self.normalize_emailid()).scalar():
                self.email_id= self.email_id.strip().lower()
                db.add(self)
                db.commit()
                db.refresh(self)
                return {"msg": f"{self.username} is added"}
            else:
                return {"message": "user already exist"}
            
    def normalize_emailid(self):
        self.email_id=self.email_id.strip().lower()
        return self.email_id
    
    
    @staticmethod
    def deleteuser(id:int):
        try:
            with SessionLocal() as db:
                deleteuser=db.query(User).filter(User.id==id).first()
                if deleteuser:
                    db.delete(deleteuser)
                    db.commit()
                    return {"message":"user as been deleted"}
                else:
                    return {"message": f"user in id number {id} not found"}
        except:
            return {"msg":"something went wrong"}
    
Base.metadata.create_all(engine)



class UserAuth(BaseModel):
    username:str
    email_id:str
    password:str


class Loginuser(BaseModel):
    username:str
    password:str


class UserBody(BaseModel):
    username:str



    
    