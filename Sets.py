Students= {"Vicky", "Hari", "Surya", "Hari", "Rajesh"}  #Sets Creation
print(Students)

# Data = {21, "Vignesh", 5.7, True}   #Sets Contains Different data types
# print(Data)

# x = {}
# print(type(x))          #It shows dictionary

# y = ()              
# print(type(y))          #It shows tuple

# z = {10, 20, 30, 40}    #It shows Set with value but without value it shows dict
# print(type(z))

# v = set()
# print(type(v))      #This is called Empty set

# Students.add(75000)     #You can add values
# print(Students)

# Students.add("Kumar")   #You can add values different data types
# print(Students)

# Students.add("Vicky")   #If you add duplicate values nothing happens it looks same
# print(Students)

# numbers = {10, 20, 30}
# numbers.update([40,50,60])      #add multiple values
# print(numbers)

# numbers.update([60, 70, 80])    #Duplicates are not allowed 
# print(numbers)

# a = {1, 2, 3, 4, 5}     #You can also add like this
# b = {6, 7, 8, 9, 10}
# a.update(b)
# print(a)

# numbers.remove(80)  #Remove the value if value empty and not match value gives error
# print(numbers)

# numbers.discard(80)   #Discard removes value specific what u gave to remove if does not match value dont show error
# print(numbers)

# remove = numbers.pop()  #remove value arbitrary and we cannot remove specific value
# print(remove)

# numbers.clear()     #Clear is removes values completely entire set still set exists
# print(numbers)

# print(type(numbers))    #Identified type 

#Membership (in, not in)                #Membership helps to show the value exist or not if exist show true else show false
# Students = ("Hari" in Students)
# print(Students)
# Students = ("Rajesh" not in Students)
# print(Students)
# Students = ("Mani" not in Students)
# print(Students)

# color = {"Blue", "White", "Black", "Blue", "Green"}     #Length identify unique value in sets and duplicate value does not count
# print(len(color))

#Union
python_class = {"Vicky", "Ragav", "Ramesh"}   #while combining also does not accept duplicate  
Sql_class = {"Harish", "Ragav", "Sushant"}
print(python_class)
print(Sql_class)

# print(python_class | Sql_class)         #Combine Sets called union This is first method using or symbol
# print(python_class.union(Sql_class))    #this is second method combine sets both same result gives

# # INTERSECTION      (Intersection helps to identify common value from set)
# print(python_class & Sql_class)
# print(python_class.intersection(Sql_class))

# # DIFFERENCE    (The differnce in sets is likely left join or right on sql shows only what is the difference meanwhile common values)
# print(python_class - Sql_class)             # it shows left join mean first set
# print(python_class.difference(Sql_class))

# print(Sql_class - python_class)
# print(Sql_class.difference(python_class))   #it shows right join mean second set

# # SYMMETRIC DIFFERENCE      (It is shows both sets data together which is not common means left and right join shows both data set without common values)
# print(python_class ^ Sql_class)
# print(python_class.symmetric_difference(Sql_class))

# SUBSET (Subset is A set value is inside in B set mean same value if same value show true else show false even one value)
# a = {1, 2, 3, 4, 11}
# b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# print(a <= b)
# print(a.issubset(b))

# SUPERSET (Superset is check same as subset but the difference between is subset check using superset, but superset is check itself wheather value is inside or not that is the difference )
# small = {10, 20, 30, 80}
# large = {10, 20, 30, 40, 50, 60, 70}

# print(large >= small)
# print(large.issuperset(small))

# DISJOINT (Disjoint is using for comparing two sets then checking the value is common or not and shows true or false)
# Mark = {79, 83, 30, 98, 60}
# Marks = {75, 81, 30, 54, 43}
# print(Mark.isdisjoint(Marks))

# # REMOVE DUPLICATES FROM SET
# District = ["Coimbatore", "Chennai", "Madurai", "Trichy", "Coimbatore", "Chennai", "Trichy", "Chennai"]
# unique = set(District)      #converting the list data into set for removing duplicates
# print(unique)

# unique = list(set(District))    #converts same data set into list 
# print(unique)