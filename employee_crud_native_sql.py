from sqlalchemy import insert
from sqlalchemy.sql import text
from sqlalchemy import create_engine #for db to connect with app
from sqlalchemy.orm import sessionmaker 
from fastapi import FastAPI, HTTPException, Depends, status, Response
from database import Base 
from sqlalchemy import Boolean, Column, Integer, String
from pydantic import BaseModel #data validation
from sqlalchemy.ext.declarative import declarative_base 
    
URL_DATABASE = 'mysql+pymysql://root:Krishna@localhost:3306/employee_details'
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

db = SessionLocal()

def insert_employee_values_using_native_sql():
    statement = text("INSERT INTO employee_data (id, name, phone, email) VALUES (13, 'David', 7854, 'david@gmail.com')")
    db.execute(statement)
    db.commit()
insert_employee_values_using_native_sql()

def insert_employee_values_using_host_variables():
    emp_dict = {
        'id' : 16,
        'name' : 'Sai Teja',
        'phone' : 55678,
        'email' : 'krishnasaiteja@yahoo.com'
    }
    statement = text("INSERT INTO employee_data (id, name, phone, email) VALUES (:id, :name, :phone, :email)")
    db.execute(statement, emp_dict)
    db.commit() 
insert_employee_values_using_host_variables()

def insert_MULTIPLE_employee_values_using_host_variables(list):
    for i in range(len(list)):
        emp_dict = list[i]
        statement = text("INSERT INTO employee_data (id, name, phone, email) VALUES (:id, :name, :phone, :email)")
        db.execute(statement, emp_dict)
    db.commit()

#prepare data and call method insert_MULTIPLE_employee_values_using_host_variables  
emp_1  = {
    "name" : "Don",
    "id" : 17,
    "phone" : 5677,
    "email" : "Don@yahoo.com"
}

emp_2  = {
    "name" : "Lily",
    "id" : 18,
    "phone" : 356899,
    "email" : "lily@hotmail.com"
}

emp_list = [emp_1,emp_2]
insert_MULTIPLE_employee_values_using_host_variables(emp_list)

