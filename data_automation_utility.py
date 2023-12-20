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

#execute 1 sql
@app.get("/EmployeeDetails/DataUtility{SQL}", status_code=status.HTTP_200_OK)
async def DataUtilityCRUD(sql_stmt : str, db:db_dependency_postgres):
    statement = text(sql_stmt)
    db.execute(statement)
    db.commit()
    return "SQL Executed Successfully"


statement_1 = {'SQL': "Select * From employee_data where id = 10"}
statement_2 = {'SQL': "Update employee_data Set name = 'Krishna Sai Teja' where id = 10"}
statement_3 = {'SQL': "Select * From employee_data where id = 10"}

SQL_QUERIES = [statement_1,statement_2,statement_3]

#print(SQL_QUERIES)

#execute multiple sql
@app.get("/EmployeeDetails/DataUtility", status_code=status.HTTP_200_OK)
async def DataUtilityCRUD(db:db_dependency_postgres):
    for SQL_QUERY in SQL_QUERIES:
        #sql = SQL_QUERIES[0]
        sql_query = SQL_QUERY.get('SQL')
        statement = text(SQL_QUERY.get('SQL'))
        if sql_query.split()[0] == 'Select':
            result = db.execute(statement)
            print(result.fetchall())
        else:
            result = db.execute(statement)
            print('No of Rows Updated:' + str(result.rowcount))
        db.commit()
    return "SQL Executed Successfully"

#To automate updating database values
#Today's problem: Applications keep their message verbagein a centralized message table ofetn thses message needs to be changed
#according to the business needs. Today in production these updates will be done manually by DBAs ofetn this is time consuming 
#and error prone and to solve this problem we created a database utility to automate it. An API is created which takes SQL's as inputs
#and executes given sql's and emails sql results automatically

