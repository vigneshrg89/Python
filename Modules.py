# Modules this is helps to reusable code from another file to file we can set filename what ever we want and the benefit is we don't need to copy the just call the function we can use code that is  works of modules 
# def add (a, b):
#     return (a + b)

# def sub(a, b):  #if you print used here two file runs output if did not use print only the main.py file output 
#     return (a - b)
# print(sub(20, 5))

# modules.py → Contains the reusable add() function
# main.py → Imports the calculator module and uses its function

# importing modules Python provides different ways to import and use code from a module

#Explanation:
# import modules imports the entire module
# modules.add() calls the add() function
# modules.subtract() calls the subtract() function

# def mul (a, b):
#     return (a * b)

#Aliases Using as
#An alias is an alternative name given to a module or an imported function,We use aliases to make names shorter or easier to use

#import modules as m	Gives the module an alias
#from modules import add as addition	Gives the imported function an alias function also we can use alias

#creating your own module 
# 1. how python finds your module because the two files are in same folder
# 2. The Important Concept: if __name__ == "__main__": this is a special variable of python it means Python automatically sets the special variable __name__ to "__main__" when you run that file directly, and this is useful for using multiple files importing this will not print everything,  example it won't print unwanted line but it when u print directly shortly i say explain you can get function from modules just because reusing code purpose so u can get function that kind of things only unwanted lines will not appear main.py that's solve
# __name__ is a special Python variable.
# When a file runs directly, __name__ becomes "__main__".
# When a file is imported, __name__ usually becomes its module name.
#
# def addition (a, b):
#     return (a + b)

# def subtract (a, b):
#     return (a - b)
# if __name__ == "__main__":
#     print("Addition and Subraction ran successfully")
#     print(addition(25, 25))
#     print(subtract(30, 25))

#practical applications example, student mark calculation   
def calculate_sum(marks):   #here i used function function for mark calculate this function will be import on main.py then you give value and other things on that file finnaly you can get value on that main.py using function from modules import you can also print the values here too but this is the purpose of modules means codereuse from another file it is called modules
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)