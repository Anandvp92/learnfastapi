from fastapi import FastAPI
from models import User,UserAuth,Loginuser,UserBody
from database import SessionLocal


app = FastAPI()



@app.post("/createuser/")
def CreateUser(user:UserAuth ):
    newuser=User(username=user.username,password=user.password,email_id=user.email_id)

    with SessionLocal() as db:
        db.add(newuser)
        db.commit()
        db.refresh(newuser)
    return {"message":user.username}

@app.post("/getuser/")
def Verifyuser(user:Loginuser):
    with SessionLocal() as db:
        dbuser = db.query(User).filter(User.username==user.username).first()
        if dbuser:
            if dbuser.get_password_verify(user.password):
                
                return {"message":[dbuser.username,dbuser.email_id,dbuser.id,dbuser.is_admin,dbuser.is_staff]}   
            else:
                return{"message":"password is wrong"}     
        else:
            return {"message":"no user was found"}

