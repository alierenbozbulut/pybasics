#Username and Password Check with while loop and break

systemuser = "admin"
systempass = "password"

while (True):
    username = input("Username : ")
    password = input("Password : ")
    if ((username == systemuser)and(password == systempass)):
        print ("Welcome...")
        break
    elif ((username != systemuser)and(password == systempass)):
        print("Username is wrong. Try Again")
    elif ((username == systemuser) and (password != systempass)):
        print("Password is wrong. Try Again")
    else:
        print("Try Again.")