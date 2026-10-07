# Students = {"Name" : "Vicky",           # Dictionary creation
#             "Age" : 21,
#             "City" : "Coimbatore",
#             "Course" : "python"}
# print(Students)

# print(Students["Name"])         # Key access means printing specific value and here we cant use index number only access with key
# print(Students["Age"])
# print(Students["City"])
# print(Students["Course"])

# Bikes = {"Bajaj" : "NS200",     # Duplicates are allowed but key should be unique name if same key name, value it will replaces the old value
#         "Hero" : "Extreme",
#         "Yamaha" : "R15",
#         "Bajaj1" : "NS200",
#         "Bajaj2" : "NS400"}
# print(Bikes)

# print(Students["City"])                      #This is print specific values
# print(Students.get("City"))                 #This is also print specific values but safer method if exist show value does not exist show none but normal method if does not exist show error
# print(Students.get("Email"))        #if no key like this show none
# print(Students.get("Email", "Not Available"))   #we can costomize the "none" key

# student = {'Name' : 'Vicky',    #we can crete dictionary or anything in python single quotes ''
#            'Age' : 21}
# print(student)

# student ['City'] = 'Coimbatore' #Add key and values in dictionary
# student ['Course'] = 'Excel'
# print(student)

# student ['Age'] = 22    # This is the example syntax of modifies values in dictionary if exist modify does not exist add key value
# student ['City'] = 'Chennai'
# print(student)

# student.pop('Course')   # pop removes the key value pair by key name
# print(student)

# student.popitem()   #popitem removes only last key value pair
# print(student)

# del student['City']     # delete is remove the key value pair by its key name and this is a syntax
# print(student)

# student.clear() # clear is empty the key and values completely
# print(student)

# print(type(student))    #type identify

# print(student.keys())   # It is helps to print key only what is inside dictionary

# print(student.values()) # It is helps to print only values what is inside in dictionary

# print(student.items())  # Items helps to print key and values both what is inside dictionary

# student = ("Name" in student)
# student = ("Marks" not in student)
# student = ("Marks" in student)
# print(student)

# print(student.__len__())    #identify lenth of dictionary
# print(len(student))     #identify lenth of dictionary both works

# student.update({                        #update helps to add new value and modifies existing values
#     "Email" : "vignesh123@gmail.com",
#     "Age" : 21
# })
# print(student)

# CopyDic = student.copy()    #copy dictionary creation
# print(CopyDic)

# CopyDic.popitem()   #copied dictionary if you made any changes it does not affect original dictionary
# print(CopyDic)
# print(student)

# Employees = {
#         'Employee1' : {'Name' : 'Vignesh',      #Nested Dictionary Creation it means main dictionary holds inside multiple dictionary
#                  'Age' : 21,
#                  'Salary' : 50000},
#         'Employee2' : {'Name' : 'Surya',
#                  'Age' : 23,
#                  'Salary' : 25000}
# }
# print(Employees)

# print(Employees['Employee2']['Salary'])     #To access value syntax

# for key in student:     #key only prints through for loop and values only we cant print
#     print(key)
    
# for key , values in student.items():    #key and values print through for loop 
#     print(key , values)

#Dictionary Comprehension (Dict Comprehension is shortcut creating dictionary)
# Squares = {}        #Empty Dictionary
# for num in range(1, 6):    #Normal Shortcut 
#     Squares[num] = num * num
#     print(Squares)
    
# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}   #Dictionary og shortcut even num square
# Squares1 = {num  : num * num  for num in numbers if num % 2 == 0}
# print(Squares1)

# numbers1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}  #Dictionary og shortcut Odd num cube
# Cube = {num : num * num * num for num in numbers1 if num % 2 == 1}
# print(Cube)

# Product = {'Name' : 'Mobile',   #Dictionary is commonly used for structred information
#            'Category' : 'Electronic',
#            'Price' : 200000,
#            'Quantity' : 10}
# print(Product)

# print(Product['Price'])

# #TEST
# Student = {'Vicky' : 95,
#            'Ravi' : 56,
#            'Manoj' : 87,
#            'Suresh' : 75,
#            'Hari' : 88}
# print(Student)

# print(Student.keys())
# print(Student.values())
# Student['Rahul'] = 98
# print(Student)
# Student['Suresh'] = 48
# print(Student)

# Score = {Name : marks for Name, marks in Student.items() if marks <= 80}
# print(Score)

# products = {
#     "Laptop": 55000,
#     "Mouse": 800,
#     "Keyboard": 1500,
#     "Monitor": 12000,
#     "Headphones": 2500
# }

# print(products)

# High = {Objects : price for Objects, price in products.items() if price >= 2000}
# print(High)

# students = {
#     "Vicky": 85,
#     "Arun": 72,
#     "Kumar": 91,
#     "Ravi": 68,
#     "Manoj": 95,
#     "Rahul": 78
# }
# print(students)

# High_mark = {Name : Marks + 5 for Name, Marks in students.items() if Marks >= 80}
# print(High_mark)