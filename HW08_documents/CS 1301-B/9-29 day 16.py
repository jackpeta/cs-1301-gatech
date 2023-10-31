# day 16 9-29 cs1301

import random
import string
import math

tas = ["Chris","Avinash","Naomi","Collin","Priya"]

random_index = random.randrange(0,5)
print(tas[random_index])

random_gpa = random.random() * 4.0 # 0 to 3.9999

print("{} has a {} gpa".format(tas[random_index], round(random_gpa,1)))

# write a function that returns a count of how many ta names end in a vowel



def count_vowels(alist):
    count = 0
    for name,major in alist:
        if name[-1] in "aeiouAEIOU":
            count +=1
    return count
            



tas = [("Naomi","CS"), ("Alice","Physics"),("Collin","CM")]
print(count_vowels(tas))

ta_dict = {"Priya":12, "Naomi":11, "Collin":13}

print(ta_dict["Naomi"])

food_dict = {"pizza":1200, "celery":12, "cupcake":800}

print(food_dict["celery"])

newdict = {}
newdict["cat"] = "cute"
newdict{"dog"} = "cuter"
print(newdict)
newdict["dog"] = "smart" #replace the old key value pair
    
