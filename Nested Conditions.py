# Nested Conditions
# marks  = 55     # nested if is using multiple if statement in 1st if statement below here maybe 1st if condition becomes false then no output will come maybe if you if + else you can get output from else 
# if marks >= 50:
#     print("Pass")
    
#     if marks >= 80:
#         print("Excellent")
        
#         if marks <= 50:
#              print("Fail")

#nested if + else       Nested if + else looks flow and here i using login code
username = "admin"
password = "1234"

Username = input("Enter Username : ")
Password = input("Enter Password : ")

if Username == username:    #this is getting input and show output method 
    if Password == password:
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Username Incorrect")    

# if username == "admin":       #this is direct method for showing output this method we don't have give input details
#     if password == "1234":
#         print("Login Successful")
#     else:
#         print("Wrong Password")        
# else:
#     print("Username Incorrect")