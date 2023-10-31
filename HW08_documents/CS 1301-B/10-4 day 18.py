# day 18 10-2 cs1301

alist = [1,2,3,[4,5]]
blist = alist
clist = alist[:] # clist is a copy
blist.append(7)
print(alist)
print(clist)


## weird thing
alist[3].append(9)
print(alist)
print(clist) #has a 9! what the flip. how.
# it's because it's a shallow copy

tas = {"Naomi":(18,4.0),"Chris":(21,3.9),"Collin":(26,4.0)}

lookup = ["Naomi", "Collin"]

# what is the average gpa of a TA in the lookup list?

total = 0.0
for name in lookup:
    total += tas[name][1]

print(total / len(lookup))

# or

total = 0.0
for name in lookup:
    age,gpa = tas[name]
    total += gpa
print(total / len(lookup))

# create a list of tas that have gpa > 3.75
high_gpas = []
for name in tas: # gives me all the keys - that's how a for loop works for a dictionary :D
    age,gpa = tas[name]
    if gpa > 3.75:
        high_gpas.append(name)

print(high_gpas)

# add the TAs favorite color to the dictionary for all the TAS in the lookup list

lookup = [("Naomi","pink"),("Collin","dark green")]

for name,color in lookup:
    tas[name] = tas[name] + (color,)
print(tas)

print(len({1:2,2:3,1:4})) # 2 - 1 is mapped twice

print(len({print("hi"):5, print("bye"):7})) # 1 - any print statement or append or whatever returns None so None is mapped twice
    
