userName = 'Dario'
password = 123

if userName == 'Dario' and password == 123:
    print("Welcome to the system "+userName)
else:
    print("Wrong Credentials, please check and try again")

if userName == 'Dario':
    lastName = 'HerrerA'
    if lastName != "Herrera":
        print("Your name is "+userName+" and your lastname is different to "+lastName)
    else:
        print("Your name is "+userName+" and your lastname is "+lastName)
else:
    print("You are not "+userName)