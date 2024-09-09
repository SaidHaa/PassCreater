import string
import random

characters  = list(string.ascii_letters + string.digits + "!@#*~()&$§ß") #buchstaben + zahlen + sonderzahlen

def generate_password():
    password_length = int(input("How long would you like your password be? "))


    random.shuffle(characters) #mischt charcters

    password = []

    for x in range(password_length): #so lang wie password soll appenden (anazhl komische zahlen)
        password.append(random.choice(characters))

    random.shuffle(password) # noch mal mischen

    password = "".join(password) # password in "hinfügen" kann man gleich in list machen normal

    print(password)


option = input("Do you want to generate a password? (yes/no): ").lower()

if option == "yes":
    generate_password()
elif option == "no":
    print("program ended")
    quit()
else:
    print("inavalid input")
    quit()










