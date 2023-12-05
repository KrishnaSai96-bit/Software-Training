from sqlalchemy import Boolean, Column, Integer, String
#from database import Base
from sqlalchemy import create_engine #for db to connect with app
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base 
from fastapi import FastAPI, HTTPException, Depends, status, Response
from pydantic import BaseModel #data validation
from typing import Annotated
#import models
#from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

#Preparing Database/Engine/Local Session
URL_DATABASE = 'mysql+pymysql://root:Krishna@localhost:3306/cookingdata'
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

#Data Models
class CookingData(Base):
    __tablename__ = 'CookingData'
    
    ID = Column(Integer, primary_key= True, index= True)
    Title = Column(String(50))
    Ingredients = Column(String(5000))
    CookingTime = Column(Integer)
    Category = Column(String(50))
    Steps = Column(String(5000)) 
    

app = FastAPI()
Base.metadata.create_all(bind=engine) 

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

class CookingData(BaseModel):
    ID: int
    Title: str
    Ingredients: str
    CookingTime: int
    Category: str
    Steps: str
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

#Post Method using ORM Model
# @app.post("/CookingData/CreateData", status_code=status.HTTP_200_OK)
# async def CreateData (CDBO: CookingData, db:db_dependency):
#     db_dao = CookingData(**CDBO.model_dump())
#     db.add(db_dao)
#     db.commit()
    
@app.post("/CookingData/CreateData", status_code=status.HTTP_200_OK)
async def CreateData (CDBO: CookingData, db:db_dependency):
    CDBO = CDBO.model_dump()
    statement = text("INSERT INTO cookingdata(ID, Title, Ingredients, CookingTime, Category, Steps) VALUES(:ID, :Title, :Ingredients, :CookingTime, :Category, :Steps)")
    db.execute(statement, CDBO)
    db.commit()