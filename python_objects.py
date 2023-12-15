class Employee:
    def __init__(self, name, id, phone, email):
        self.name = name
        self.id = id
        self.phone = phone
        self.email = email
        
class Car:
        def __init__(self, manufacturer, model, year, color):
            self.manufacturer = manufacturer
            self.model = model
            self.year = year
            self.color = color 
            
def print_details():
    employee_1 = Employee('Teja', 1, '8978987928', 'grk.saiteja@yahoo.com')
    employee_2 = Employee('John',2,'864-3344','asd@hotmaiil.com')
    employee_3 = Employee('Alex',3,'2490-2347','tgh@outlook.com')
    employee_4 = Employee('Lilly', 4,'7982-3458','hjk@yahoo.com')
    employee_5 = Employee('Sai',5 ,'2349-3457','ghj@yahoo.com')
    employees = [employee_1, employee_2, employee_3, employee_4, employee_5]
    print(employee_1)
    for i in range(len(employees)):
        employee = employees[i]
        #employee.name
        print(employee.name)
        print(employee.id)
        print(employee.phone)
        print(employee.email)
    
    car_1 = Car('Kia', 'Seltos', 2020, 'White')
    car_2 = Car('Maruthi', 'Brezza', 2017, 'Red')
    car_3 = Car('Tata', 'Nexon', 2023, 'Blue')
    print(car_1)
    print(car_1.manufacturer)
    mixed_list = []
    mixed_list.append(employee_1)
    mixed_list.append(employee_2)
    mixed_list.append(employee_3)
    mixed_list.append(employee_4)
    mixed_list.append(employee_5)
    mixed_list.append(car_1)
    mixed_list.append(car_2)
    mixed_list.append(car_3)
    for i in range(len(mixed_list)):
        details = mixed_list[i]
        if isinstance(details,Employee):
            print(details.id)
            print(details.name)
            print(details.phone)
            print(details.email)
        else: 
            if isinstance(details,Car):
                print(details.manufacturer)
                print(details.model)
                print(details.year)
                print(details.color)


def object_count(list):
    employee_count = 0
    car_count = 0
    employee_list = []
    car_list = []
    for i in range(len(list)):
        details = list[i]
        if isinstance(details, Employee):
            employee_list.append(details)
            employee_count = employee_count +1
        else:
            if isinstance(details, Car):
                car_list.append(details)
                car_count = car_count +1
    message1 = "No of Employees are: " + str(employee_count) + " - " + "No of Cars: " + str(car_count)
    message2 = "No of Employees are: " + str(len(employee_list)) + " - " + "No of Cars: " + str(len(car_list))
    return message2      
        
       
def print_details_from_dict(list):
    for i in range(len(list)):
        emp = list[i]
        name = emp['name']
        id = emp['id']
        phone = emp['phone']
        email = emp['email']
        print(name)
        print(id)
        print(phone)
        print(email)
    
    return
     
        
        
    
    
    



