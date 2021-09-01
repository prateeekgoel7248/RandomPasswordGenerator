from password_creator import Password
import re
#l=int(input("input password length : "))
print("##################################")
print("Enter s for only special symbols \nEnter u for only Upper case Character\nEnter l for only lower case")
print("Enter d for only digits \nYou can also enter combination like su,ul,ld etc...\n")
print("##################################")
ch=str(input( "Enter characters : "))
l=int(input("input password length : "))
if re.search(ch,"suld"):
    password = Password(ch, l)
    password.set_the_charset()
    password.generate_password()
    print("the random password is : ", password.get_password())
else:
    print("You entered wrong characters \nPlease enter characters between 's' 'u' 'l' 'd' \n ")