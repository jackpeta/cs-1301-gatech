# day 8 cs1301-b

# how many vowels are in a particular string?

word = "beat georgia"
count = 0
for ch in word:
   if ch in "aeiouAEIOU":
       count += 1
print(count)

# build a str within a loop

# build a str of all the vowels from word
vowels = "" # start with an empty string

for ch in word:
    if ch in "aeiouAEIOU":
        vowels += ch #concatenate onto the string of vowels
print(vowels)

# what if you were told to remove the vowels from beat georgia

non_vowels = ""
for ch in word:
    if ch not in "aeiouAEIOU":
        non_vowels += ch
print(non_vowels)

# build a str containing all the letters of jackets with a space after each letter

jackets = "jackets"
jackets_spaced = ""
for ch in jackets:
    jackets_spaced += ch + " "
print(jackets_spaced)

# str is made up of individual pieces that can be accessed separately - string indexing

name = "spongebob squarepants"
#print(name[1]) # this gives p - indexing starts from 0 :D coding likes things to start from 0

print(name[0])
print(name[1])
print(name[3])

num=5
print(name[num])

# the length of the name
print(len(name))

print(name[20])
print(name[len(name) - 1]) # these 2 statements are equivalent - when we do not know the length of the string
# we can use the len function within the index itself

print("                   ")

name = "spongebobs squarepants"
for num in range(5):
    print(name[num]) # name indexed at positions 0, then 1.2.3....then 4

# build a string containing every other letter of name

newname = ""
for num in range(0,len(name),2): # let range generate the positions you need, instead of manually doing it
    newname += name[num]
print(newname)

# string slicing

# indexing only gives you one character!
# slicing gives you 0 or 1 or more characters

name = "spongebobs squarepants"
name_part1 = name[0:4]
print(name_part1)

name_part2 = name[5:7]
print(name_part2)

weird_slice = name[1:8:2] # 3rd value in the slice is the step - just like range!
print(weird_slice)

print("        ")

# slicing in a loop
for num in range(5): #0,1,2,3,4
    print(name[num:num+3])










