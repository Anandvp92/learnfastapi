from fastapi import FastAPI
from models import User,UserAuth,Loginuser,UserBody
from database import SessionLocal


app = FastAPI()



@app.post("/createuser/")
def CreateUser(user:UserAuth):
    newuser=User(username=user.username,password=user.password,email_id=user.email_id)    
    return newuser.insertdata()
    

@app.post("/getuser/")
def Verifyuser(user:Loginuser):
    with SessionLocal() as db:
        dbuser = db.query(User).filter(User.username==user.username).first()
        if dbuser:
            if dbuser.get_password_verify(user.password):                
                return {"message":"User loggedin"}   
            else:
                return{"message":"password is wrong"}     
        else:
            return {"message":"no user was found"}
        
        
@app.delete("/userdelete/{userid}")        
def userdelete(userid:int):
    return User.deleteuser(id=userid)   

 
@app.get("/listusers/")
def listusers():
    
    with SessionLocal() as db:
        allusers=db.query(User).all()
        if allusers:
            return {"msg":[ user.displayuser() for user in allusers]}
        else:
            return {"msg":"No users found"}