#Arithmatic Operators
# a = 20
# b = 6

# print(a + b)    #Addition
# print(a - b)    #Sub
# print(a * b)    #Mul
# print(a / b)    #Div
# print(a // b)   #Floor Div (Whole num after div)
# print(a % b)    #Modules    (Remainder)
# print(a ** b)   #Power

#Comparison Operator
# a = 21
# b = 10

# print(a == b)
# print(a != b)
# print(a > b )
# print(a < b )
# print(a >= b)
# print(a <= b)

# Assignment Operator
# a = 5
# a += 3
# a -= 3
# a *= 3
# a /= 3
# a //= 3
# a %= 3
# a **= 3
# print(a)

#Logical Operator
Age = 21

if Age > 18 and Age < 25:   #AND Operator Should Both condition true
    print("True")

if Age > 18 or Age < 18:    #OR Operator This OR That
    print("True")

print(not True)     #not true

#Membership
Name = "Vicky"

print("Vic" in Name)      #We can identify this is there or not shows true or false
print("Si" not in Name)

#Identify
a = [10 , 20]       
b = a
print(a is b)
print(a is not b) 

#Bitwise Operator only pending