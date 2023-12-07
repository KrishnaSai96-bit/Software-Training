import pywhatkit

# Defining the Phone Number and Message

def push_whatsapp_message(input_message: str):
    phone_number = "+918978987928"
    # message = "On Call Alert from Teja: There is a Production Issue Severity 1 and you must join the on call bridge asap"
    pywhatkit.sendwhatmsg_instantly(phone_number, input_message)
    print("Message sent!")
    

