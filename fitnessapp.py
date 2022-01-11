#dashboard.py
import verify
import signup
import object

print("Hello user, would you like to create an account with us, type 'yes' please")
response = input()

if response == "yes":
    print("great, whats your name?")
    user = input()
    print("wonderful, whats your password ?")
    password = input()

else:
    done = False 
    count = 0
    accountdatabase = []
    databasefile = open("database.txt","a")
    while(not done):
        print("ok, would you like to create a new account with us?")
        response = input()
        if (response == "yes"):
            accountdatabase.append(signup.signupfunc())
            print("congratulation, you've made an account!!")
            print("username is", accountdatabase[count].username)
            databasefile.write(accountdatabase[count].username)
            databasefile.write(accountdatabase[count].password)
            print("you live in",accountdatabase[count].location)
        else:

            print("ok bye")
            done = True
        count = count +1
        
        
        
 #signup.py       
        
def signupfunc ():
    print("hello user, thank you for creating an account with us")
    name = input()
    print("what is your age?")
    age = input()
    print("what is your email?")
    email = input()
    print("what is your password?")
    password = input()
    print("what is your location?")
    location = input
    print("what is your current_weight?")
    current_weight = input()
    print("what is your target_weight?")
    target_weight = input()
    user = object.User(name,email,password,age,location,current_weight,target_weight)
    return user 
