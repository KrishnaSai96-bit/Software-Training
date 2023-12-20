from sqlalchemy import insert
from sqlalchemy.sql import text
from sqlalchemy import create_engine #for db to connect with app
from sqlalchemy.orm import sessionmaker 
from fastapi import FastAPI, HTTPException, Depends, status, Response
from database import Base 
from sqlalchemy import Boolean, Column, Integer, String
from pydantic import BaseModel #data validation
from sqlalchemy.ext.declarative import declarative_base 
from typing import Annotated
from sqlalchemy.orm import Session
import csv
from csv import DictReader

#Postgres
URL_DATABASE_POSTGRES = 'postgresql://postgres:Krishna@localhost/cookingdata'

#MySQL
URL_DATABASE_MYSQL = 'mysql+pymysql://root:Krishna@localhost:3306/cookingdata'

#Postgres
engine_postgres = create_engine(URL_DATABASE_POSTGRES)
SessionLocal_Postgres = sessionmaker(autocommit = False, autoflush = False, bind = engine_postgres)
Base = declarative_base()
db_postgres = SessionLocal_Postgres()

#My SQL
engine_mysql = create_engine(URL_DATABASE_MYSQL)
SessionLocal_MySQL = sessionmaker(autocommit = False, autoflush = False, bind = engine_mysql)
Base = declarative_base()
db_mysql = SessionLocal_MySQL()

# instantiate app
app = FastAPI()
#Postgres
#app_postgres = FastAPI()
Base.metadata.create_all(bind=engine_postgres)

#MySQL
#app_mysql = FastAPI()
Base.metadata.create_all(bind=engine_mysql) 

class CookingData(Base):
    __tablename__ = 'CookingData'
    
    ID = Column(Integer, primary_key= True, index= True)
    Title = Column(String(500))
    Ingredients = Column(String(5000))
    CookingTime = Column(Integer)
    Category = Column(String(500))
    Steps = Column(String(5000))

class CookingData(BaseModel):
    ID: int
    Title: str
    Ingredients: str
    CookingTime: int
    Category: str
    Steps: str
    
#Postgres    
def get_db_postgres():
    db_postgres = SessionLocal_Postgres()
    try:
        yield db_postgres
    finally:
        db_postgres.close()

db_dependency_postgres = Annotated[Session, Depends(get_db_postgres)]

#MySQL    
def get_db_mysql():
    db_mysql = SessionLocal_MySQL()
    try:
        yield db_mysql
    finally:
        db_mysql.close()

db_dependency_mysql = Annotated[Session, Depends(get_db_mysql)]

@app.get("/CookingData/GetCookingData", status_code=status.HTTP_200_OK)
async def GetData(db:db_dependency_mysql):
    statement = text("SELECT * FROM cookingdata.cookingdata")
    result = db.execute(statement)
    recipe = result.fetchall()
    recipe_list = []
    for i in range(len(recipe)):
        recipe_dict = {'ID':recipe[i][0], 'Title':recipe[i][1], 'Ingredients':recipe[i][2], 'CookingTime':recipe[i][3], 'Category':recipe[i][4], 'Steps':recipe[i][5]}
        recipe_list.append(recipe_dict)
    ########################
    for employee in recipe_list:
        with open('RecipeBook.csv', 'w') as f:
            w = csv.DictWriter(f, employee.keys())
            w.writerows(recipe_list)
    ########################
    return recipe_list


