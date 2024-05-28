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
    
    @staticmethod
    def get_password_hash(password):
        password= pwd_context.hash(password)
        
        
        
Base.metadata.create_all(engine)



class UserAuth(BaseModel):
    username:str
    email_id:str
    password:str
    
    