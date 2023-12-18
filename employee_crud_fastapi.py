# from sqlalchemy import insert
# from sqlalchemy.sql import text
# from sqlalchemy import create_engine #for db to connect with app
# from sqlalchemy.orm import sessionmaker 
# from fastapi import FastAPI, HTTPException, Depends, status, Response
# from database import Base 
# from sqlalchemy import Boolean, Column, Integer, String
# from pydantic import BaseModel #data validation
# from sqlalchemy.ext.declarative import declarative_base 
# from typing import Annotated
# from sqlalchemy.orm import Session

# URL_DATABASE = 'mysql+pymysql://root:Krishna@localhost:3306/employee_details'
# engine = create_engine(URL_DATABASE)
# SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
# Base = declarative_base()
# db = SessionLocal()

# # instantiate app
# app = FastAPI()
# Base.metadata.create_all(bind=engine) #creates tables in MySQL database based on the definitions in model.py

# class EmployeeData(Base):
#     __tablename__ = 'employee_data'

#     id = Column(Integer, primary_key=True, index=True) #first column in db, want to be able to index (faster performance)
#     name = Column(String(50)) #instantiate string with varchar 50
#     phone = Column(Integer)
#     email = Column(String(50))

# class EmployeeBO(BaseModel):
#     id: int
#     name: str
#     phone: int
#     email: str
    
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# db_dependency = Annotated[Session, Depends(get_db)] #db and class

# #Native SQL Method
# @app.post("/EmployeeDetails/CreateEmployeeData", status_code=status.HTTP_201_CREATED)
# async def create_recipe(employeeBO: EmployeeBO, db:db_dependency):
#     employeeBO = employeeBO.model_dump()
#     statement = text("INSERT INTO employee_data (id, name, phone, email) VALUES (:id, :name, :phone, :email)")
#     db.execute(statement, employeeBO)
#     db.commit()
    
# #create new metod using orm (w/o sql)
# #ORM Method
# @app.post("/EmployeeDetails/CreateEmployeeData_Using_ORM", status_code=status.HTTP_201_CREATED)
# async def create_recipe(employeeBO: EmployeeBO, db:db_dependency):
#     db_employeeDAO = EmployeeData(**employeeBO.model_dump())
#     db.add(db_employeeDAO)
#     db.commit()