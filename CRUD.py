
From: Srini Chelimilla <srini.chelimilla@gmail.com>
Sent: Friday, December 15, 2023 11:24 AM
To: Dad <chelimilla@hotmail.com>
Subject: crud operations file
 
All code is in one file - but function calls should actually be in the presentation layer.


from 
sqlalchemy import 
insert

from 
database import 
engine, SessionLocal

from 
sqlalchemy.sql 
import text



db = 
SessionLocal()



class 
Employee:

    def 
__init__(self, 
name, id, 
phone, email):

        self.name =
name

        self.id =
id

        self.phone =
phone

        self.email =
email



employee_1 = 
Employee('Jim', 
1, '123-456-789', 
'abbc.def@yahoo.com')

employee_2 = 
Employee('John',2,'111-222-333','asd@hotmaiil.com')

employee_3 = 
Employee('Alex',3,'455-513-798','tgh@outlook.com')



employees = [employee_1,
employee_2, 
employee_3]



def 
insert_values(l):

    for 
i in 
range(len(l)):

        employee = 
l[i]



        # print(vars(employee))



        statement = 
text("INSERT INTO employees_info(name, id, phone, email) VALUES(:name, :id, :phone, :email)")

        db.execute(statement,
vars(employee))

        db.commit()



def 
retrieve_value_by_id(input_id:int):

    statement = 
text("SELECT * FROM employees_info WHERE id=:a")

    result = 
db.execute(statement, {"a":input_id})

    employee = 
result.fetchall()

    print(employee)



def 
retrieve_all_values():

    statement = 
text("SELECT * FROM employees_info")

    result = 
db.execute(statement)

    all_employees = 
result.fetchall()

    print(all_employees)



# insert_values()

# retrieve_value_by_id(1)

# retrieve_all_values()
