# day 15 cs1301 9-27

tup1 = ("CAT",)
tup2 = ("dog",)
tup3 = (2,)
new_tup = tup1 + tup2 + tup3
print(new_tup)

ta_tup = ("Chris", "Liding", 10)
# how can i change the rating? - gotta rebuild it
ta_tup = ta_tup[0:2] + (ta_tup[2]-1,)
print(ta_tup)

# how could we build a tuple from scratch?
atup = ()
for num in range(5):
    atup += (num,) #concatenate tuples containing each of the numbers onto the tup you are building
print(atup)
    
# actually the parenthesis arent even required - only the comma is required to make it a tuple

ta_tup = ("Chris","Liding",10)

fname,lname,rating = ta_tup
print(fname)

def split_name(name):

    name_list = name.split()
    (fname,lname) = (name_list[0], name_list[1])

    return (fname,lname)

for tup in enumerate("jackets"):
    print(tup)

for position,letter in enumerate("jackets"):
    print(position)
    print(letter)

for position,letter in enumerate("jackets"):
    if position % 2 == 0:
        print(letter)

# print(enumerate(cat)) gives a numerate object ???

import math
print(math.sqrt(7))
print(math.pi)

import string
print(string.punctuation)
# if letter in string.punctuation:  ## very useful for evaluating if its a punctuation

print(string.ascii_letters)
