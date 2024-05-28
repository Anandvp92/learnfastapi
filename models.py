from pydantic import BaseModel
from datetime import datetime, timedelta
from database import Base,engine
from sqlalchemy import Column,Integer,String,Boolean,DateTime
from sqlalchemy.orm import Session
from passlib.context import CryptContext

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
        self.get_password_hash()


    def get_password_hash(self):
        self.password= pwd_context.hash(self.password)
        
    def get_password_verify(self,unhashedpassword :str) ->bool:
        return pwd_context.verify(unhashedpassword,self.password)
    
        
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



    
    