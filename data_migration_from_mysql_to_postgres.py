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
URL_DATABASE_POSTGRES = 'postgresql://postgres:Krishna@localhost/employee_details'

#MySQL
URL_DATABASE_MYSQL = 'mysql+pymysql://root:Krishna@localhost:3306/employee_details'

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

class EmployeeData(Base):
    __tablename__ = 'employee_data'
    id = Column(Integer, primary_key=True, index=True) #first column in db, want to be able to index (faster performance)
    name = Column(String(50)) #instantiate string with varchar 50
    phone = Column(Integer)
    email = Column(String(50))

class EmployeeBO(BaseModel):
    id: int
    name: str
    phone: int
    email: str
    
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

#Native SQL Method
#Postgres
@app.post("/EmployeeDetails/CreateEmployeeDataPostgres", status_code=status.HTTP_201_CREATED)
async def create_employee_data(employeeBO: EmployeeBO, db:db_dependency_postgres):
    employeeBO = employeeBO.model_dump()
    statement = text("INSERT INTO employee_data (id, name, phone, email) VALUES (:id, :name, :phone, :email)")
    db.execute(statement, employeeBO)
    db.commit()
    

#@app.post("/EmployeeDetails/CreateEmployeeDataFromCSVFile", status_code=status.HTTP_201_CREATED)
@app.get("/EmployeeDetails/InsertFileData{FielName}", status_code=status.HTTP_200_OK)
async def InsertFIleData(fileName: str, db:db_dependency_postgres):
    with open(fileName, 'r') as f: 
       dict_reader = DictReader(f)
       entries = list(dict_reader)
    for entry in entries:
        statement = text("INSERT INTO employee_data (id, name, phone, email) VALUES (:id, :name, :phone, :email)")
        db.execute(statement, entry)
        db.commit()
    return "datainsertedsuccesfully"
        
@app.get("/EmployeeDetails/GetEmployeeData", status_code=status.HTTP_200_OK)
async def GetData(db:db_dependency_mysql):
    statement = text("SELECT * FROM employee_details.employee_data")
    result = db.execute(statement)
    employees = result.fetchall()
    employee_list = []
    for i in range(len(employees)):
        emp_dict = {'id':employees[i][0], 'name':employees[i][1], 'phone':employees[i][2], 'email':employees[i][3]}
        employee_list.append(emp_dict)
    ########################
    #Once employee list is populated with all the database values same is returned to a file before returning to fast api
    
    for employee in employee_list:
        with open('mycsvfile.csv', 'w') as f:
            w = csv.DictWriter(f, employee.keys())
            w.writerows(employee_list)
    ########################
    
    return employee_list


