from sqlalchemy import Boolean, Column, Integer, String
from database import Base
from sqlalchemy import create_engine #for db to connect with app
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base 
from fastapi import FastAPI, HTTPException, Depends, status, Response
from pydantic import BaseModel #data validation
from typing import Annotated
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
from fastapi.middleware.cors import CORSMiddleware

#Preparing Database/Engine/Local Session
URL_DATABASE = 'mysql+pymysql://root:Krishna@localhost:3306/knowledgehub'
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()
db = SessionLocal()

#Data Models
class KnowledgeHub(Base):
    __tablename__ = 'knowledge_hub'
    
    Message_ID = Column(Integer, primary_key= True, index= True)
    Technology_Type = Column(String(45))
    Exception_Type = Column(String(500))
    Exception_Title = Column(String(1000))
    Description = Column(String(5000))

app = FastAPI()
Base.metadata.create_all(bind=engine) 
origins = ['http://localhost:3000',]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

class KnowledgeHub(BaseModel):
    Message_ID: int
    Technology_Type: str
    Exception_Type: str
    Exception_Title: str
    Description: str
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/KnowledgeHub/InsertFileData/{FileName}", status_code=status.HTTP_200_OK)
async def InserFielData(FileName: str, db:db_dependency):
    with open(FileName, 'r') as f: 
       dict_reader = DictReader(f)
       entries = list(dict_reader)
    for entry in entries:
        statement = text("INSERT INTO knowledge_hub(Message_ID, Technology_Type, Exception_Type, Exception_Title, Description) VALUES(:Message_ID, :Technology_Type, :Exception_Type, :Exception_Title, :Description)")
        db.execute(statement,entry)
        db.commit()
    return "Data Inserted Succesfully"

@app.post("/KnowledgeHub/CreateData/", status_code=status.HTTP_200_OK)
async def CreateData (EXBO: KnowledgeHub, db:db_dependency):
    EXBO = EXBO.model_dump()
    statement = text("INSERT INTO knowledge_hub(Message_ID, Technology_Type, Exception_Type, Exception_Title, Description) VALUES(:Message_ID, :Technology_Type, :Exception_Type, :Exception_Title, :Description)")
    db.execute(statement, EXBO)
    db.commit()
    
@app.get("/KnowledgeHub/GetData/", status_code=status.HTTP_200_OK)
async def GetData(db:db_dependency):
    statement = text("SELECT * FROM knowledgehub.knowledge_hub")
    result = db.execute(statement)
    exceptions = result.fetchall()
    exceptions_list = []
    for i in range(len(exceptions)):
        exceptions_dict = {'Message_ID':exceptions[i][0], 'Technology_Type':exceptions[i][1], 'Exception_Type':exceptions[i][2], 'Exception_Title':exceptions[i][3], 'Description':exceptions[i][4]}
        exceptions_list.append(exceptions_dict)
    return exceptions_list

@app.get("/KnowledgeHub/GetData_Using_ID/{Message_ID}", status_code=status.HTTP_200_OK)
async def GetData(Message_ID: str, db:db_dependency):
    statement = text("SELECT * FROM knowledgehub.knowledge_hub where Message_ID = :Message_ID")
    result = db.execute(statement, {'Message_ID': Message_ID})
    exceptions = result.fetchall()
    exceptions_list = []
    for i in range(len(exceptions)):
        exceptions_dict = {'Message_ID':exceptions[i][0], 'Technology_Type':exceptions[i][1], 'Exception_Type':exceptions[i][2], 'Exception_Title':exceptions[i][3], 'Description':exceptions[i][4]}
        exceptions_list.append(exceptions_dict)
    return exceptions_list

@app.get("/KnowledgeHub/GetData_Using_Technology_Type/{Technology_Type}", status_code=status.HTTP_200_OK)
async def GetData(Technology_Type: str, db:db_dependency):
    statement = text("SELECT * FROM knowledgehub.knowledge_hub where Technology_Type = :Technology_Type")
    result = db.execute(statement, {'Technology_Type': Technology_Type})
    exceptions = result.fetchall()
    exceptions_list = []
    for i in range(len(exceptions)):
        exceptions_dict = {'Message_ID':exceptions[i][0], 'Technology_Type':exceptions[i][1], 'Exception_Type':exceptions[i][2], 'Exception_Title':exceptions[i][3], 'Description':exceptions[i][4]}
        exceptions_list.append(exceptions_dict)
    return exceptions_list

@app.put("/KnowledgeHub/Update_ExceptionsData/{Message_ID}", status_code=status.HTTP_200_OK)
async def Update_ExceptionsData(Message_ID: int, exceptiondataBO: KnowledgeHub, db:db_dependency):
    exceptiondataBO = exceptiondataBO.model_dump()
    exceptiondataBO['Message_ID'] = Message_ID
    statement = text("UPDATE knowledgehub.knowledge_hub SET Message_ID = :Message_ID, Technology_Type = :Technology_Type, Exception_Type = :Exception_Type, Exception_Title = :Exception_Title, Description = :Description WHERE Message_ID =:Message_ID")
    db.execute(statement, exceptiondataBO)
    db.commit()