systemuser = "admin"
systempass = "admin"

user = input("User: ")
password = input("Password: ")

if ((systemuser == user)and(systempass == password)):
    print("Sign-in was successful.")
elif ((systemuser != user)and(systempass == password)):
    print("Username is wrong!")
elif ((systemuser == user)and(systempass != password)):
    print("Password is wrong!")
else:
    print("Try Again.")
