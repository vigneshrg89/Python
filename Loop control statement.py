# Break
# num = 1
# while num <= 10:
#     print(num)
    
#     if num == 7:  #Break is using for stop the loops even condition true 
#         break
#     num += 1

# names = [ "Vignesh", "Surya", "Hari", "Mani"]   #break we can use string also here is the example
# for name in names:
#     if name == "Hari":
#         break
#     print(name)

#Continue
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if num == 5:      #continue is using for skips the iteration continue and break is called loop control statement
#         continue
#     print(num)

names = [ "Vignesh", "Surya", "Hari", "Mani"]   #here is example of using continue with strings 
for name in names:
    if name == "Hari":
        continue
    print(name)

#Pass
# for i in range(1, 6): #pass is using for placeholders it means it does not make changes like continue, break but it is actually do nothing, it is using example : if you created a function but the is empty so if you leave it like empty then error will come so if you use pass below the function it does not become error that's solve, it is also called placeholder
#     if i == 3:
#         pass
#     print(i)
    
# for i in range(1, 11):
#     if i == 3 or i == 7:  #you can use continue for multiple values skiping here is the syntax of skipping multiple values using continue
#         continue          #here we are used or because same variable name so it should not take values equal if variable name difference we can use and
#     print(i)