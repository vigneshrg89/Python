#Function A function is a reusable block of code that performs a specific task, 
# Instead of writing the same code repeatedly, you can create a function and call it whenever needed

# def welcome():    #def is a function keyword welcome is function name
#     print("Hello Vicky!")
    
# welcome() #function called
# welcome() #function called multiple times it uses is repeat code multiple times
# welcome()

# def calcualte_total(amount, price):   #arugument passing in parameters amount, price is parameters 25,30 is arguments
#     print(amount + price) #adds the value
    
# calcualte_total(25, 30)   #calls function

# def students(name, marks):    #multiple parameters using
#     print(name, marks)

# students("Vignesh", 97)
# students("Ravi", 85)

#return
# def square(num):  #using return is In Python, return sends a result back from a function so you can store it or use it later
#     return num * num  #identify square
# result = square(6)
# result1 = square(5)   #here we reused the return

# print(result)
# print(result1)

#default parameters
# def greet(name="Bro"): #default value insertion method
#     print("Hello", name)

# greet() #default value exeuted here
# greet("Vignesh")    #without default value 

# def calculated_price(price, quantity = 2):
#     print(price * quantity)
    
# calculated_price(200)

# def calculated_price(price, qty = 2):
#     return price * qty
# result  = calculated_price(300)
# result = calculated_price(250, 5)
# print(result)

# def employee(name, salary):   #keyword argument means you can give value by parameters and advantage is you can give any order means unorder it will print orderly like how you gave parameters in function
#     return (name, salary)
# result = employee(salary= 50000, name= "Vicky")
# print(result)

# def employee(name, salary):
#     print(name, salary)
# employee(salary = 45000, name = "Arun")

#postional arguments vs keyword arguments but you should use first positional argument positional means natural argument passing you can use both but first positional
# def employee(name, age, salary):    #here is example using both positional and keyword arguments
#     print(name, age, salary)
# employee("Vicky", salary = 50000, age = 21, )

# *args stores multiple arguments *is what matters
# def calculate_sum(*args): args is like a variable  it stores multiple arguments
#     print(sum(args))  #adds the value
# calculate_sum(10,20)  #same function handle different types of numbers
# calculate_sum(10,20,30,40,50,60)  multiple values

# def num(a,b):   #this shows error because 2 parameters 3 arguments that's why using *args it helps single parameters stores multiple arguments
#     print(a + b)
# num(10,20, 30)  
    
# **Kwargs  kwargs is stores different keyword arguments also it acts as dictionary output also comes like dictionary output
# def employee(**kwargs):   #kwargs we have to give key and value like dictionary
#     print(kwargs)

# employee(name = "Arun", Age =21, Salary= 25000)

# def emp(**kwargs):  #display each detail you can see through output
#     for key, values in kwargs.items():
#         print( key, ":", values)
# emp(name = "arun", age = 21, salary = 25000)

#Local variable vs Global variable
# college = "ABC COLLEGE"   #global variable is used inside and outside function but local variable is we can only use inside function

# def details():
#     Name = "VIGNESH"  #local variable 
#     print(Name)
#     print(college)
# details() #function calling here
# print(college)

#Global keyword it means we can change global varible value in inside function and it changes the global variable value
# salary = 20000

# def increse_salary(): #with global
#     global salary
#     salary = 25000
    
# increse_salary()
# print(salary)

# a = 10    #without global

# def num():
#     a = 20
#     print(a)

# num()
# print(a)

#Lambda lambda is a small function it reduses our work instead of using def function or normal function i showed difference below
# square = lambda number: number * number   #finding square using lambda
# print(square(8))
# print(square(5))

# def square(number): #finding square using function that's difference between lambda and function
#     return number * number
#     print(square)
    
# result = square(8)
# print(result)

# Function calling another function it means one function runs another one main function below is example and here we can use multiple calling i used add, sub, multiply called by showdetails() function it is also a kind of reuse code we can save time and avoid multiple lines code, it is a method of function calling another function
def multiply(a, b):
    return a * b

def sub(c, d):
    return c - d

def add(e, f):
    return e + f

def showdetails():
    result = multiply(5, 6)
    result1 = sub(10, 5)
    result2 = add(25, 25)
    print(result)
    print(result1)
    print(result2)

showdetails()