import al_validations

CCNumber = input("Enter a Credit Card Number:")
message = al_validations.validate_credit_card_number(CCNumber)
print (message)

EmailID = input("Enter Email ID:")
message = al_validations.validate_email_id(EmailID)
print(message)