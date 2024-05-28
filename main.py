from views import app
import uvicorn
from models import User


if __name__=="__main__":
    uvicorn.run("main:app",port= 8000,reload=True)