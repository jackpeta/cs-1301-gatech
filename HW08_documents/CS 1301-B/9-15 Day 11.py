# day 11 cs 1301

name = "Chris"
print(name[0].isalpha() and name[0].isDigit()) #F False

# write a function that returns True if the first and last letter in the param are the same and False otherwise

def same_f_and_l(astr):

    return astr[0] == astr[-1]
