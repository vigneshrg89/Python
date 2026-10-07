Students = ("Vicky", "Arun", "Sathish", "Praveen", "Ranjith")   #Tuple Creation
print(Students)

# print(Students[0])      #Tuple indexing just like list indexing 
# print(Students[2])      #positive index
# print(Students[4])
# print(Students[-2])     #Negative index 

# print(Students[:2])     #Slicing in tuples same as list
# print(Students[2:])
# print(Students[2:5])
# print(Students[:])
# print(Students[-1])
# print(Students[-3:])
# print(Students[:-3])

# Details = ("Vignesh", "Coimbatore", 21, "vignesh123@gmail.com")     #Tuple Unpacking : this is convert without variable values into with variable values

# Name, City, Age, Email_Address = Details    #This all steps are tuple unpacking
# print(Name)
# print(City)
# print(Age)
# print(Email_Address)

#Tuple Main 2 methods
# Electronics = ("Mobile", "Laptop", "Refridgerator", "Washing Machine", "Mobile")    #Tuple Creation
# print(Electronics.count("Mobile"))      #Count is counting values which is repeated multiple times same as list
# print(Electronics.index("Laptop"))      #Index is identifying index num by value name same as list

# #Tuple Operations
# print(len(Electronics))     #len counting total tuple inside values same as list

# print("Vicky" in Students)      #in is helps identify data inside exist or not if exist show true else false same as list
# print("Vicky" not in Students)

# Combine_tuples = Students + Electronics     # + combine two tuples in a new tuple name after merge if you change anything in that tuple not changes happen in new tuple same as list
# print(Combine_tuples)

# print(Students * 2)     #repeat the tuple
# print(" Vicky " * 3)    #repeat the tuple value

Numbers = (19, 21, 26, 70, 97, 45)      #Tuple creation
print(Numbers)

print(min(Numbers))     #show least value
print(max(Numbers))     #show high value
print(sum(Numbers))     #totals the tuple values

#List vs Tuple
Subjects = ["English", "Maths", "Science", "Data Structue", "Python"]   #This example is for proving list can change, tuple cannot change values only read and access or operations we can't modify tuple like list
print(Subjects)
Subjects.append("Excel")
print(Subjects)

Months = ("Jan", "Feb", "Mar", "Apr", "May")
print(Months)
Months.remove("Jan")
print(Months)