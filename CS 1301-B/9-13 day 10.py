# day 10 cs1301

print("cat".upper())
# .upper is a function method - the input is before the dot instead of in the parentheses

print("cats are {}".format("cute"))

print("C123PO".lower()) #lowercase!

print("C123PO".replace("1","X")) # replaces all instances of a certain character with another :0

print("C123PO111".find("C")) # finds the first occurance and gives it to you in terms of chararcter index, so this will be 0

print("C123PO111".find("C123")) # will still return 0, which is the starting position of the string.

print("C123PO111".find("C2")) # returns -1, which means that .find did not find anything

name = "Chris"
if name.find("C") == -1:
    print("not in there")
else:
    print("fun ta")
# could also use a loop

# what is the difference between .find and .index? they both return the index

# print("cat".find("z")) #returns -1
# print("cat".index("z")) # error occurs

# what if you need to uppercase just the third and fourth characters of spongebob?

name = "spongebob"
 # this wont work

#name[2] = name[2].upper
 #name[3] = name[3].upper

 # what you gotta do is rebuild the string

print(name)
# this rebuilding thing can be used in a loop to change an individual character

number_to_change = 5
name = name[0:5] + name[number_to_change].upper() + name[number_to_change+1:]
print(name)

# .isalpha() - boolean for is it a character
# .isdigit() - boolean for is it a digit
# .isupper() - boolean for is it an uppercase
# .islower() - boolean for is it a  lowercase



# coding example - change all values in a string to capital X

sentence = "TAs are fun"

newstr = ""

for ch in sentence:
    if ch in "aeiouAEIOU":
        newstr += "X"
    else:
        newstr += ch

sentence = newstr
print(newstr)
