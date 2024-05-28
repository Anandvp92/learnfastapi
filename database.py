from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///./test.db")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()