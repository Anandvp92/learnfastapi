from fastapi import FastAPI
from models import User,UserAuth
from database import SessionLocal


app = FastAPI()



@app.post("/createuser/")
def CreateUser(user:UserAuth ):
    h=User.get_password_hash(user.password)
    newuser=User(**user.dict())
    newuser.password=h
    with SessionLocal() as db:
        db.add(newuser)
        db.commit()
        db.refresh(newuser)
    return {"message":user.username}


