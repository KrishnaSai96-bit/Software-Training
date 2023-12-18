from sqlalchemy import insert
from sqlalchemy.sql import text
from sqlalchemy import create_engine #for db to connect with app
from sqlalchemy.orm import sessionmaker 
from fastapi import FastAPI, HTTPException, Depends, status, Response
from database import Base 
from sqlalchemy import Boolean, Column, Integer, String
from pydantic import BaseModel #data validation
from sqlalchemy.ext.declarative import declarative_base 

class EmployeeData(Base):
    __tablename__ = 'employee_data'

    id = Column(Integer, primary_key=True, index=True) #first column in db, want to be able to index (faster performance)
    name = Column(String(50)) #instantiate string with varchar 50
    phone = Column(Integer)
    email = Column(String(50))
    
URL_DATABASE = 'mysql+pymysql://root:Krishna@localhost:3306/employee_details'
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()
db = SessionLocal()


#insert_MULTIPLE_employee_values_using_host_variables(emp_list)

def insert_employee_values_using_ORM(list):

    for i in range(len(list)):
        employee_dict = list[i]
        
        MyID = employee_dict['id']
        MyName = employee_dict['name']
        MyPhone = employee_dict['phone']
        MyEmail = employee_dict['email']
        
        employee = EmployeeData(id = MyID, name = MyName , phone = MyPhone, email = MyEmail)
        #ORM Command to insert data into table
        db.add(employee)
    
    #employee_2 = EmployeeData(id = 19, name = 'Lotus', phone = '4567', email = 'lotus@yahoo.com')
    #db.add(employee_2)
    
    db.commit()

#This is forntend data preperation and method invocation
emp_1  = {
    "id" : 22,
    "name" : "Megha",
    "phone" : 7777,
    "email" : "Megha@yahoo.com"
}

emp_2  = {
    "id" : 23,
    "name" : "Adarsh",
    "phone" : 9999,
    "email" : "adarsh@hotmail.com"
}

emp_list = [emp_1,emp_2]

#invoking method
insert_employee_values_using_ORM(emp_list)