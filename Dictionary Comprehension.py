# Basic syntax dict compre..  this is useful for creeting dict shorter way bracket must {first key : values}
# numbers = [1, 2, 3, 4, 5]   #using dict compre..
# result = {n : n * 10 for n in numbers}
# print(result)

# without dict compre
# numbers = [1, 2, 3, 4, 5]
# squares = {}

# for n in numbers:
#     squares[n] = n*n

# print(squares)

#Transforming Keys and Values we can use dictionary comprehension to change both the keys and values of an existing dictionary
# Syntax {new_key: new_value for key, value in dictionary.items()}
# products = {
#     "pen": 10,
#     "book": 50,
#     "bag": 500
# }
# result = {product.upper(): price + price for product, price in products.items()}
# print(result)

# Dictionary Comprehension with if We can use if to filter dictionary items based on a condition
# prices = {
#     "pen": 10,
#     "book": 50,
#     "bag": 500,
#     "pencil": 5,
#     "shoes": 800
# }
# result = {product : price for product, price in prices.items() if price > 100}
# print(result)

# Dictionary Comprehension with if-else We can use if-else to assign different values depending on a condition
#syntax {key: value_if_true if condition else value_if_false for item in iterable}
# marks = {
#     "Arun": 85,
#     "Bala": 35,
#     "Kumar": 70,
#     "Ravi": 25
# }

# result = {name : "Pass" if mark > 50 else "Fail" for name, mark in marks.items()}
# print(result)

# employees = {
#     "Arun": 25000,
#     "Bala": 15000,
#     "Kumar": 30000,
#     "Ravi": 18000
# }

# result = {Salary : "High Salary" if amount > 20000 else "Low Salary" for Salary, amount in employees.items()}
# print(result)

# Using .items() with Existing Dictionaries, items() it is useful for The .items() method returns the key and value together for each dictionary entry
# student = {
#     "Arun": 85,
#     "Bala": 90,
#     "Kumar": 75
# }

# print(student.items())

# updated_mark = {name : mark + 10 for name, mark in student.items()}
# print(updated_mark)

# products = {
#     "pen": 10,
#     "book": 50,
#     "bag": 200
# }
# result = {product : amount + 20 for product, amount in products.items()}
# print(result)

#Nested Dictionary Comprehensions   nested dict compre it means another dict inside 
# employees = ["Arun", "Bala"]
# departments = ["Sales", "IT"]

# combine = {name: {department : 0 for department in departments}for name in employees}   #Here we can give any value strings, numbers instead of zero, zero also you can use that is example
# print(combine)

#Readability and practical applications
products = ["Pen", "Book", "Bag"]   #dictionary comprehensions are useful for creating dictionaries from existing data, transforming values, and filtering records
prices = [10, 50, 200]

result = {products[i] : prices[i] for i in range(len(products))}        #when you have to combine two list into one dict use this method 
print(result)
# How does it work?

# products[0]: prices[0] → "Pen": 10
# products[1]: prices[1] → "Book": 50
# products[2]: prices[2] → "Bag": 200

#len() → counts items
# range() → generates numbers
# i → stores each index
# zip() → pairs corresponding items from two lists
result = {product: price for product, price in zip(products, prices)}       #this also work using zip pairs corresponding items from two list 
print(result)