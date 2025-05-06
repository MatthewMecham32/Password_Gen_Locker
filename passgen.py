

import random
import string
import re
from passlocker import create_account, main

def auto_generate_password():
#Generates a random password with the following characteristics
#Accepts prompt from user to receive input for deciding:
#length
#Upper and Lower
#Numbers
#Special Characters
    Pass_length = int(input("Enter your desired length:"))
    print(f"Length is: {Pass_length}")

    upper_lower = input("Is mixed case required? yes or no: ")
    print(f"Upper and Lower choice is: {upper_lower}")

    numbers = input("Are numbers required? yes or no: ")
    print(f"Number choice is: {numbers}")

    special = input("Are special characters required? yes or no: ")
    print(f"Special Character choice is: {special}")
    #Determine password requirements
    if numbers == "yes":
        num = random.choice(string.digits)
        #print(f"Number choice: {num}")
    else:
        num = ""
    
    if special =="yes":
        special = random.choice(string.punctuation)
        #print(f"Special choice: {special}")
    else:
        special = ""
    
    if upper_lower == "yes":
        up_low = random.choice(string.ascii_letters)
    else:
        up_low = ""

    #Add required variables into chars.
    #This guarantees that at least one of each of the required inputs
    chars = str(num) + special + up_low

    #create a list of all possible characters
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    #for loop to create requried number of characters
    for i in range(Pass_length):
        #randomly adds ch
        chars = chars + random.choice(alphabet)

    char_list = list(chars)
    random.shuffle(char_list)
    password = "".join(char_list)
    return password



def self_generate_password():
    meet_reqs = "no"
    while meet_reqs =="no":
        print("Let's specify the requirements for your password")

        Pass_length = int(input("Enter your minimum length:"))
        print(f"Length is: {Pass_length}")

        Pass_upper_lower = input("Is mixed case required? yes or no")
        print(f"Upper and Lower choice is: {Pass_upper_lower}")

        Pass_numbers = input("Are numbers required? yes or no: ")
        print(f"Number choice is: {Pass_numbers}")

        Pass_special = input("Are special characters required? yes or no: ")
        print(f"Special Character choice is: {Pass_special}")

        password = input("Please type your password")
        meet_reqs = "no"

        if len(password) < Pass_length :
            meet_reqs_length = "no"
            print("The password is not long enough")
        else:
            meet_reqs_length = "yes"

        if Pass_special == "yes":
            if re.search(r'[^a-zA-Z0-9]', password):
                meet_reqs_special = "yes"
            else:
                meet_reqs_special = "no"
                print("There are no special characters")

        if Pass_upper_lower == "yes":
            if any(char.isupper() for char in password) and any(char.islower() for char in password):
                print("String contains both uppercase and lowercase letters!")
                meet_reqs_mixed = "yes"
            else:
                meet_reqs_mixed = "no"
                print("String does not contain both cases.")
        
        if any(char.isdigit() for char in password):
            print("The string contains a number!")
            meet_reqs_num = "yes"
        else:
            meet_reqs_num = "no"
            print("No numbers found.")
        
        if any(var == "no" for var in [meet_reqs_num, meet_reqs_length, meet_reqs_special, meet_reqs_mixed]):
            meet_reqs = "no"
        else:
            meet_reqs = "yes"

    return password  





create_password = input("Would you like to create your own password? yes or no")
print(f"Create your own password is: {create_password}")

if create_password == "yes":
    random_password = self_generate_password()
else:
    random_password= auto_generate_password()

print(f"Generated password:{random_password}")

add_locker = input("Would you like to add a password to the locker? yes or no")

if add_locker == "yes":
    username = input("Please enter a username")
    create_account(username, random_password)
    main()
else:
    print("No password added to locker")
    exit()
    