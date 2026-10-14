#Built-in Modules
#Built-in modules are ready-made Python modules that provide useful functions. We can import and use them instead of writing everything ourselves

#math.sqrt(25) → square root of 25.
# math.factorial(5) → 5 × 4 × 3 × 2 × 1.
# math.pi → value of π

# import math   #used for mathematical operations
# print(math.sqrt(144))
# print(math.factorial(6))
# print(math.pi)

# import random     #Used to generate random value 
# print(random.randint(1, 100)) #randint is not a variable it is a keyword

# name = ["vicky", "surya", "hari", "mani", "saravana"] #list also we can use random
# print(random.choice(name))    #choice is not variable name it is a keyword

import datetime #Used to work with dates and times

today = datetime.date.today() #today date display
print(today)

now = datetime.datetime.now()   #today date and time display 
print(now)