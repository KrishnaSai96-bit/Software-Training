import al_validations
import python_objects

# CCNumber = input("Enter a Credit Card Number:")
# message = al_validations.validate_credit_card_number(CCNumber)
# print (message)

# EmailID = input("Enter Email ID:")
# message = al_validations.validate_email_id(EmailID)
# print(message)

employee_1 = python_objects.Employee('Teja', 1, '8978-9876', 'grk.saiteja@yahoo.com')
employee_2 = python_objects.Employee('John',2,'864-3344','asd@hotmaiil.com')
employee_3 = python_objects.Employee('Alex',3,'2490-2347','tgh@outlook.com')
employee_4 = python_objects.Employee('Lilly', 4,'7982-3458','hjk@yahoo.com')
employee_5 = python_objects.Employee('Sai',5 ,'2349-3457','ghj@yahoo.com')

car_1 = python_objects.Car('Kia', 'Seltos', 2020, 'White')
car_2 = python_objects.Car('Maruthi', 'Brezza', 2017, 'Red')
car_3 = python_objects.Car('Tata', 'Nexon', 2023, 'Blue')

#mixed_list = []

# mixed_list.append(employee_1)
# mixed_list.append(car_1)
# mixed_list.append(employee_2)
# mixed_list.append(employee_3)
# mixed_list.append(car_2)
# mixed_list.append(employee_4)
# mixed_list.append(car_3)
# mixed_list.append(employee_5)
# mixed_list.append(employee_1)

#message = python_objects.object_count(mixed_list)

#print(message)

#dict menthod
# emp_1  = {
#     "name" : "Teja",
#     "id" : 1,
#     "phone" : 8978987928,
#     "email" : "grk.saiteja@yahoo.com"
# }

# emp_2 = {
#     "name" : "John",
#     "id" : 2,
#     "phone" : 334454392,
#     "email" : "john@gamil.com"
# }

emp_1 = vars(employee_1)
emp_2 = vars(employee_2)
emp_3 = vars(employee_3)
emp_4 = vars(employee_4)
emp_5 = vars(employee_5)

emp_list = [emp_1, emp_2, emp_3, emp_4, emp_5]

python_objects.print_details_from_dict(emp_list)