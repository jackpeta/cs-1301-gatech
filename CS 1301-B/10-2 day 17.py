# day 17 10-02 cs1301

adict = {"A":"APPLE", "a":"ape", 0:"zero"}
# print(adict[1]) # 1 is the key - not the index! so this will not work.

if 1 in adict:
    print(adict[1])

# dictionaries are mutable
adict[0] = "Zero"
print(adict)

adict["Chris"] = "funny"
adict["Naomi"] = "head TA"
adict["A"] = "Arvin"
print(adict)

# create a dictionary from two lists
names = ["Jo","Bo","Lou"]
ages = [15, 23, 5]
newdict = {}
for position, name in enumerate(names):
    newdict[name] = ages[position]

print(newdict)

# write code to build a dict that maps each index in a name to the later
# that is at that spot - hint: use enumerate

letter_dict = {} # {0:"N", 1:"a", 2:"o", 3:"m", 4:"i"}
name = "Naomi"
for position,letter in enumerate(name):
    letter_dict[position] = name[position]
print(letter_dict)

book_dict = {"It":"King", "1984":"Orwell", "Emma":"Austen"}

#title = input("Enter book title: ")
#print(book_dict[title])

# print out all the authors of books taht start with the letter E
for title in book_dict.keys():
    if title[0].lower() == "e":
        print(book_dict[title])
        
