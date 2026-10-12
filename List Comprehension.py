#List comprehension this is helps to create new list short method existing sequence or iterable
# numbers = []  #This is normal method
# for i in range(1, 6):
#     numbers.append(i) #normal when using append is must but list comprehension is not need
#     print(numbers)
    
# numbers = [i for i in range (1,6)]    #This is using list comprehension
# print(numbers)

# square = [num * num for num in range(1,6)]    #square the value using list comprehension
# print(square)

# cube = [i * i * i for i in range(1,6)]    #Cube the value using list comprehension
# print(cube)

#List comprehension with condition(if)  everytime using list comprehension the expression is always comes before for loop 
# numbers = []          #if here using reason is for filtering here i was used for get even numbers and this is normal method using with if
# for i in range(1, 11):
#     if i % 2 == 0:
#         numbers.append(i)

# print(numbers)
    
# even_numbers = [i for i in range(1, 11) if i %2 == 0] # list comprehension with if
# print(even_numbers)

# number =[i for i in range(1, 11) if i %2 == 1 if i > 5]   # we can also use multiple condition
# print(number)

# number =[i for i in range(1, 11) if i > 5]
# print(number)

# numbers = []
# for i in range(1, 11,):
#     if i %2 == 1:
#        if i > 5:
#             numbers.append(i)
# print(numbers)
            
# numbers1 = [1, 3, 5, 7, 9, 11]

# result = [ i for i in numbers1 if i > 5]
# print(result)

# numbers = [v for v in range(1,33) if v %3 ==0]
# print(numbers)

#List comprehension with if and else, if we have double goals here even odd double goals so here we used if and else, and when we use if and else both syntax will be change look the difference between if and if + else concept
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = []
# for i in numbers: #normal method
#     if i %2 == 0:
#         result.append("Even")
#     else:
#         result.append("Odd")
# print(result)

# number = ["Even" if i %2 == 0 else "Odd" for i in range(1,11)]    #list comprehension with if and else method
# print(number)

# numbers = [10, 15, 20, 25, 30]
# result = ["Pass" if i > 20 else "Fail" for i in numbers]
# print(result)

#list comprehension with strings it helps to extract every letter from words
# word = "Python"
# letters = [i for i in word]
# print(letters)

# word = "Excel"
# letters = [char for char in word]
# print(letters)

# word = "Data analyst"
# result = [i for i in word if i in "aeiou"]    #we can also filter specific letter this is example
# print(result)

#Upper case the list value here is example
# names = ["vicky", "raj", "hari"]
# upper_case = [name.upper() for name in names]
# print(upper_case)

#nested loop in list comprehension A nested loop means one loop inside another loop
# numbers = []

# for i in [1, 2]:
#     for j in [10, 20]:    #normal method
#         numbers.append((i, j))
        
# print(numbers)
        
# numbers = [(i, j) for i in [1, 2] for j in [10, 20]]   #using list comprehension
# print(numbers)

# numbers = []  normal method to add values in nested loop
# for i in [1, 2, 3]:
#     for j in [5, 6, 7]:
#         numbers.append(i +j)
        
# print(numbers)

# numbers = [(i + j) for i in [1,2,3] for j in [5, 6, 7]]   #add values in nested loop using list comprehension
# print(numbers)

#working with existing list using list comprehensions it is useful for we can use an existing list to create a new list by transforming or filtering its elements
# sales = [1200, 800, 2500, 600, 3000, 1500]  #filtering list
# high_sales = [high for high in sales if high >= 1000]
# print(high_sales)

# price = [100, 200, 300, 400]    #transforming list
# total = [amount + 50 for amount in price]
# print(total)

# gst = [add + 50 for add in sales]   
# print(gst)

#Nested List Comprehensions it means A nested list is a list that contains other lists
# marks = [[70, 80], [60, 90], [85, 95]]
# result = [n for row in marks for n in row if n >= 80]
# print(result)

# Remember
# for row in numbers → takes each inner list.
# for n in row → takes each number from that inner list.
# n → adds each number to the new list 

# numbers = [       #Here, we have one main list containing three inner lists it is called nested list comprehension
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# result = []
# for row in numbers:
#     for n in row:
#         result.append(n)

# print(result)

# result = [n for row in numbers for n in row]
# print(result)

# Readability and practical applications This tried to say code program logically it means use code simply understand for eveyone and use easy method compared to which is complicated method that's solve
sales = [500, 1200, 800, 2500, 3000]
result = [amount + amount for amount in sales if amount >= 1000]  
print(result)