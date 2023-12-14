employee_1 = ['GRK',1,'4567-7123','abc@gmail.com']
employee_2 = ['Teja',2,'5746-2222','xyz@gmail.com']
employee_3 = ['John',3,'864-3344','asd@hotmaiil.com']
employee_4 = ['Alex',4,'2490-2347','tgh@outlook.com']
employee_5 = ['Lilly',5,'7982-3458','hjk@yahoo.com']

employees = [employee_1, employee_2, employee_3, employee_4, employee_5]
print(employees)

employee_6 = ['Sai',6,'2349-3457','ghj@yahoo.com']
employees.append(employee_6)
print(employees)

# for employee in employees:
#     #employee = employees[i]
#     print(employee)
    
# for i in range(len(employees)):
#     employee = employees[i]
#     print(employee)
    
for i in range(len(employees)):
    employee_name = employees[i][0]
    employee_id = employees[i][1]
    employee_phone_number = employees[i][2]
    employee_email_id = employees[i][3]
    print(employee_name)
    print(employee_id)
    print(employee_phone_number)
    print(employee_email_id)
    
for i in range(len(employees)):
    employee = employees[i]
    for j in range(len(employee)):
        employee_details = employee[j] 
        print(employee_details)
        
employees.clear()
print(employees)
    
    
    
    
    