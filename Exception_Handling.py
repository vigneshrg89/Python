# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     print("Result :", a / b)

# except:
#     print("error occured")

# print("program completed")

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     print("result :", a/b )
    
# except ValueError:
#     print("Enter valid number")
# except ZeroDivisionError:
#     print("Zero can't divide")
# except TypeError:
#     print("incompatiable error data type used")

# else:
#     print("Success")
    
# try:
#     number = int(input("Enter a number: "))
#     print("Result:", 100 / number)

# except ValueError:
#     print("Please enter a valid number!")

# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# else:
#     print("Calculation successful!")

# finally:
#     print("Program execution finished!")

try:
    sales1 = int(input("Enter a amount: "))
    sales2 = int(input("Enter a amount: "))
    print("Program started")
    print("Total sales",sales1 + sales2)
    print("avg", sales1 + sales2 / 2)

except ValueError:
    print("Please enter valid number")
    
else:
    print("Success")
    
finally:
    print("Program finished")