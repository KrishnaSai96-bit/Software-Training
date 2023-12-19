from sqlalchemy import Boolean, Column, Integer, String
from database import Base
from sqlalchemy import create_engine #for db to connect with app
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base 
from fastapi import FastAPI, HTTPException, Depends, status, Response
from pydantic import BaseModel #data validation
from typing import Annotated
#import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from sqlalchemy import insert
from sqlalchemy.sql import text
from csv import DictReader
import matchstatement
from sqlalchemy import exc
import communication
import pywhatkit
import models2

#Preparing Database/Engine/Local Session
URL_DATABASE = 'mysql+pymysql://root:Krishna@localhost:3306/cookingdata'
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()
db = SessionLocal()

#Data Models
class CookingData(Base):
    __tablename__ = 'CookingData'
    
    ID = Column(Integer, primary_key= True, index= True)
    Title = Column(String(500))
    Ingredients = Column(String(5000))
    CookingTime = Column(Integer)
    Category = Column(String(500))
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
     
@app.get("/CookingData/GetData", status_code=status.HTTP_200_OK)
async def GetData(db:db_dependency):
    statement = text("SELECT * FROM cookingdata.cookingdata")
    result = db.execute(statement)
    recipe = result.fetchall()
    recipe_list = []
    for i in range(len(recipe)):
        recipe_dict = {'ID':recipe[i][0], 'Title':recipe[i][1], 'Ingredients':recipe[i][2], 'CookingTime':recipe[i][3], 'Category':recipe[i][4], 'Steps':recipe[i][5]}
        recipe_list.append(recipe_dict)
    return recipe_list

@app.get("/CookingData/GetIDandTitle", status_code=status.HTTP_200_OK)
async def GetData(db:db_dependency):
    try: 
        statement = text("SELECT cookingdata.ID, cookingdata.Title FROM cookingdata.cookingdata")
        result = db.execute(statement)
        recipe = result.fetchall()
        recipe_list = []
        for i in range(len(recipe)):
            recipe_dict = {'ID':recipe[i][0], 'Title':recipe[i][1]}
            recipe_list.append(recipe_dict)
        return recipe_list
    except exc.SQLAlchemyError as e:
        return (type(e))

@app.get("/CookingData/GetID{ID}", status_code=status.HTTP_200_OK)
async def GetData(ID: int, db:db_dependency):
    statement = text("SELECT * FROM cookingdata.cookingdata where ID = :ID")
    #TODO: Here the except code block is not working and unable to show the exceptions 
    try:    
        result = db.execute(statement, {'ID': ID})
    except:
        # exc.SQLAlchemyError as e:
        # error = str(e.__dict__['orig'])
        print ("BUNNU")
        # print (error)    
    else:
        recipe = result.fetchall()
        recipe_dict = {'ID':recipe[0][0], 'Title':recipe[0][1], 'Ingredients':recipe[0][2], 'CookingTime':recipe[0][3], 'Category':recipe[0][4], 'Steps':recipe[0][5]}
    finally:
        return recipe_dict
       
@app.get("/CookingData/GetCode{Code}", status_code=status.HTTP_200_OK)
async def GetData(Code: int, db:db_dependency):
    detail = matchstatement.DisplayErrorCode(Code)
    raise HTTPException(status_code = Code, detail = detail, headers = {"X-Error": "My Custom Error"})
  
@app.get("/CookingData/InsertFileData{FielName}", status_code=status.HTTP_200_OK)
async def InserFielData(FileName: str, db:db_dependency):
    with open(FileName, 'r') as f: 
       dict_reader = DictReader(f)
       entries = list(dict_reader)
    for entry in entries:
        statement = text("INSERT INTO cookingdata(ID, Title, Ingredients, CookingTime, Category, Steps) VALUES(:ID, :Title, :Ingredients, :CookingTime, :Category, :Steps)")
        db.execute(statement,entry)
        db.commit()
    return "datainsertedsuccesfully"

@app.get("/CookingData/GetRecipeForGivenID{ID}", status_code=status.HTTP_200_OK)
async def GetData(ID: int, db:db_dependency):
    statement = text("SELECT * FROM cookingdata.cookingdata where ID = :ID")
    result = db.execute(statement, {'ID': ID})   
    recipe = result.fetchall()
    recipe_dict = {'ID':recipe[0][0], 'Title':recipe[0][1], 'Ingredients':recipe[0][2], 'CookingTime':recipe[0][3], 'Category':recipe[0][4], 'Steps':recipe[0][5]}
    ingredients = {'INGREDIENTS':recipe[0][2]}
    recipe = {'RECIPE_STEPS':recipe[0][5]}
    message = str(ingredients).replace("{","").replace("}", "") + "  " + str(recipe).replace("{","").replace("}", "")
    communication.push_whatsapp_message(message)
    return "Success Message"

#No Fast API Method
@app.get("/CookingData/GetIDNoFastAPI/" , status_code=status.HTTP_200_OK)
async def GetData(db:db_dependency):
    # ID: int
    input_id_dict = {
        "MyID" : 5
    }
    statement = text("SELECT * FROM cookingdata.cookingdata where ID = :MyID")
    #TODO: Here the except code block is not working and unable to show the exceptions 
    try:    
        result = db.execute(statement, input_id_dict)
    except:
        # exc.SQLAlchemyError as e:
        # error = str(e.__dict__['orig'])
        print ("BUNNU")
        # print (error)    
    else:
        recipe = result.fetchall()
        recipe_dict = {'ID':recipe[0][0], 'Title':recipe[0][1], 'Ingredients':recipe[0][2], 'CookingTime':recipe[0][3], 'Category':recipe[0][4], 'Steps':recipe[0][5]}
    finally:
        return recipe_dict
