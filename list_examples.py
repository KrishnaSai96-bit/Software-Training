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

def sum_of_list():
    list = [5,20,7,150,9,12,200]
    sum = 0
    for x in list:
        sum = sum + x
    print(sum)
    average = sum/len(list)
    print(average)
    list.sort()
    print(list)
    list.reverse()
    print(list)
    list.remove(12)
    print(list)
    list.pop(4)
    print(list)
sum_of_list()