# def is_positive_integer(x):
#     return x > 0

# number = int(input("Enter an integer: "))
# if is_positive_integer(number):
#     print(f"{number} is a positive integer!")
# else:
#     print(f"{number} is not a positive integer!")
    
def string_capitalize(s):
    return s.capitalize()

def string_casefold(s):
    return s.casefold()

def string_find(DataEntered,find_string):
    return DataEntered.find(find_string)

def string_center(s):
    return s.center(22)

def string_count(s):
    return s.count("Monday")

def string_encode(s):
    return s.encode()

def string_endswith(s):
    return s.endswith(".")

def string_expandtabs(s):
    return s.expandtabs(2)

def string_format(s):
    return s.format(price = 49)

def string_format_map(s):
    return s.format_map()

def string_index(s):
    return s.index("-")

def string_isalnum(s):
    return s.isalnum()

def string_isalpha(s):
    return s.isalpha()

def string_isascii(s):
    return s.isascii()

def string_isdecimal(s):
    return s.isdecimal()

def string_isdigit(s):
    return s.isdigit()

def string_isidentifier(s):
    return s.isidentifier()

def string_islower(s):
    return s.islower()

def string_isnumeric(s):
    return s.isnumeric()

def string_isprintable(s):
    return s.isprintable()

def string_isspace(s):
    return s.isspace()

###########################################################################
#To find the Domain Name for a given email id we follow the following steps
def get_domain_name(EmailIDEntered):
    at_postion = EmailIDEntered.find("@")
    if (at_postion == -1):
        domainvalue = "Invalid Email ID"
    else: 
        length = len(EmailIDEntered)
        domainvalue = EmailIDEntered[at_postion+1:length+1]
    return domainvalue
#print (domain_name(DataEntered))
##########################################
def domain_name_arrays(Emails):
    for i in Emails:
        domain_value = get_domain_name(i)
        print(domain_value)
# EmailID_1 = input("Enter a EmailID1:")
# EmailID_2 = input("Enter a EmailID2:")
# EmailID_3 = input("Enter a EmailID3:")
# EmailID_4 = input("Enter a EmailID4:")
# EmailID_5 = input("Enter a EmailID5:")
# Emails = [EmailID_1, EmailID_2, EmailID_3, EmailID_4, EmailID_5]
# domain_name_arrays(Emails)
###################################################################
def validate_credit_card_number(CCNumber):
    if (len(CCNumber) == 19):
        if ((CCNumber [4] == '-') and (CCNumber [9] == '-') and (CCNumber [14] == '-')):
            message = "Valid CC Number is Entered"
        else:
            message = "Invalid CC NUmber. Please Enter Dashes(-) after every 4 Numbers"
    else:
        message = "Invalid CC NUmber.CC Number must be 19 Digits"
    return message
##################################################################

def validate_email_id(EmailID):
    at_postion = EmailID.find('@')
    dot_postion = EmailID.rfind('.')
    print (at_postion)
    print (dot_postion)
    if (at_postion > 0 and dot_postion > (at_postion +1)):
        message = "Valid Email ID is entered"
    else:
        message = "Invalid Email ID is Entered"
    return message



    

#DataEntered = input("Enter a String:")
# print (domain_name(DataEntered))
#print (string_capitalize (DataEntered))
#print (string_casefold (DataEntered))
#print (string_find (DataEntered, find_string))
#print (string_center (DataEntered))
#print (string_count (DataEntered))
#print (string_encode (DataEntered))
#print (string_endswith (DataEntered))
#print (string_expandtabs (DataEntered)) #Doubt
#print (string_format (DataEntered)) #Doubt
#print (string_format_map (DataEntered)) #Doubt
#print (string_index (DataEntered))
#print (string_isalnum (DataEntered))
#print (string_isalpha (DataEntered))
#print (string_isascii (DataEntered))
#print (string_isdecimal (DataEntered))
#print (string_isdigit (DataEntered))
#print (string_isidentifier (DataEntered))
#print (string_islower (DataEntered))
#print (string_isnumeric (DataEntered))
#print (string_isprintable (DataEntered))
#print (string_isspace ("  "))





















