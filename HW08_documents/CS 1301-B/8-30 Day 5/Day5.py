# 8-30 Day 5 CS 1301-B

def circ_area(radius):
    area = 3.14159 * radius **2
    return area

circ_area(5)
#print(circ_area(5))

print(3>5) #bool statement that is false

print(3 == 3.0) #python calculates the value - they are equal despite int vs float

print("cat" < "dog") #this is true because of alphabetical order! (more than= lower on in the dictionary) (less than = further up in the dictionary)

# order of characters is determined by the Ascii code which yo dont needa know for cs1301

print(3<5 and 3>2) # requires both to be true (DISCRETE MAAAATH)

print(3<5 or 3<1) # requires at least one to evaluate to True (DISCREEEEETE)

value = 3 > 5 and not 2 < 7 or 9 > 1
print(value) # value will be true because order goes not > and > or and the or statement is true

# write a statement that prints True if the number num is between 4 and 7 inclusive

num = 5
print(num >= 4 and num <= 7) #correct
##print(num >= 4 and <= 7) # this will print a syntax error because you need two boolean expressions and '<=7' is not a bool versus 'num >= 4'

print("-------------------------")

age = 19
if age >= 18 and age <= 99:
    print("go vote")
    print("vote for cs1301")
else:
    print("no voting for you")

if True:
    print("always true")


if age > 17:
    print("you can go to college")
elif age >= 14:
    print("you can go to high school")
else:
    print("no school for you")















    
