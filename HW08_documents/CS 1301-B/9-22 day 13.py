# day 13 cs1301 advanced lists

names = ["priya","andre","chris"]

# append always appends the pararmeter onto the list before the dot
names.append("Naomi")
print(names)

# insert always inserts at a particular position in the list
names.insert(0, "naomi") # all other names shift over
names.insert(12, "alice") # if index too high, insert at end
names.insert(-1,"avinash") #inserts at 1 before the last (instead of the last :( ) in this example it's before alice
names.insert(len(names),"ramya") # inserts at the last position :D (could also use .append()
print(names)

 # del names[1]
print(names)

names.remove("andre") # removes the first occurance of a specific value from the list

# del names[20] gives an error - out of the range
# del names[-1] deletes last char of list

names.sort()
print(names)

nums = [1,4,2]
sorted_nums = sorted(nums)
print(nums)
print(sorted_nums)

nums.reverse()
print(nums)

tas = [("Chris",10],["Priya",10],["Andre",10]]

for item in tas:
    if item[1] == 10:
        print(item[0]) # checks to see if each ta is rated 10/10, prints the name if it's true
