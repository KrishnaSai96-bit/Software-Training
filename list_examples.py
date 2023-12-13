# def list_example1():
#     registration_list = [["Teja", 27], ["John", 45], ["Alex", 9], ["Tom", 60]]
#     adult_list = []
#     child_list = []
#     for Entry in registration_list:
#         age = Entry [1]
#         if (age > 10):
#             adult_list.append(age)
#         else:
#             child_list.append(age)
            
#     print(adult_list)
#     print (len(adult_list))
    
#     print(child_list)
#     print (len(child_list))
    
# list_example1()

# sum = 0
# list[0]
# sum = sum + list[0]

list = [5,10,15,20,25,30]
print("The Original List is : " + str(list))
res = []
for ele in list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)
print ("List Integer Summation : " + str(res))