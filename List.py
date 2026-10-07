#List

Bikes = ["Bajaj", "Yamaha", "ktm", "Suzuki", "Tvs"]     #list creation
print(Bikes)    #print the list
# print(Bikes[0])     #print index value positive
# print(Bikes[2])
# print(Bikes[-1])    #print index value negative 
# print(Bikes[-3])
# Bikes[3] = "Royal Enfield"      #Replace the value
# print(Bikes)
# print(Bikes[-2])
# Bikes[4] = "BMW"
# print(Bikes[4])
# Bikes.append("Aprilla")     #append
# Bikes.append("TVS")
# Bikes.append("Honda")
# print(Bikes)

Student_Name = ["Vicky", "Hari", "Surya"]   #list creation
print(Student_Name)

Student_Name.insert(2, "Niranjan")  #insert value in list by custom index position
Student_Name.insert(1, "Ranjith")
Student_Name.insert(3, "Rajesh")
Student_Name.append("Vicky")        #add values in list end
print(Student_Name)

# Student_Name.remove("Hari")       #remove values in list by value 
# Student_Name.remove("Rajesh")
# print(Student_Name)

# Student_Name.pop(1)       #remove values in list by index number
# Student_Name.pop()        #remove values in list end  
# print(Student_Name)

# Student_Name.clear()      #empty the list values totally
# print(Student_Name)

print(len(Student_Name))    #count values in list starts from 1 not 0

print("Vicky" in Student_Name)  #in using for values is inside or not Shows (TRUE or FALSE)
print("Arun" in Student_Name)

print(Student_Name.count("Vicky"))      #count is using for if repeated values inside counting like numbers 2 if no value as you mentioned shows 0
print(Student_Name.count("Aravind"))

print(Student_Name.index("Niranjan"))      #index is showing index position of value 
print(Student_Name.index("Vicky"))

# num = [50, 40, 30, 20, 10]
# num.sort()                               #sort is ascending the numbers and align char to alphabets order
# print(num)

# num.reverse()                      #reverse is using for flip the values or reverse the values but not ascending or descending
# print(num)

# Student_Name.sort()
# print(Student_Name)

# Student_Name.reverse()
# print(Student_Name)

# Students = Student_Name.copy()        #copy the list like duplicate but if modify duplicate list cannot change in og list
# print(Students)

# Students.insert(3, "Sri")
# print(Students)
# print(Student_Name)

# Student_Name.append(["Nithish", "Mani", "Saravana"])      #multiple values adding by append
# print(Student_Name)
# Student_Name.remove(["Nithish", "Mani", "Saravana"])      #multiple values remove by remove
# print(Student_Name)

# Student_Name.extend(Bikes)            #extend is merge the list2 into list1 but after merge if u modify list2 does not change happen in list1
# print(Student_Name)

list1 = [10,20,30,40,50]
list2 = [60,70,80,90,100]
print(list1)
print(list2)

list3 = list1 + list2           #+combine the both list into another new named list it is also same extend after merge not changes happen in new list
print(list3)

# print(list1[2:])              #slicing is shows values by index num what we gave
# print(list1[:3])
# print(list1[1:4])
# print(list1[:])

# print(min(list3))     #shows least value
# print(min(list1))
# print(min(list2))

# print(max(list2))     #shows high value
# print(max(list1))
# print(max(list3))

# print(sum(list1))     #sum is add the list values numbers
# print(sum(list2))
# print(sum(list3))

for list in list1:      #for using lists in shows values output one by one num and string one by one not same line that's solve 
    print(list)
    
for student in Student_Name:
    print(student)