# day 12 cs1301

ta_list = ["Chris", 200, [1,2,3], True]
print(ta_list)

nums = [1,3,5,6,2]

for num in nums:
    print(num * 2)

print(nums[2]) #int
print(nums[2:4]) #list of ints - class<list>
print(nums[0:1]) # a list containing the 0th item - a slice will ALWAYS give a sublist

names = ['Melinda','Chris','Collin','Andre']
print(names[0][0])

print('                           ')

for name in names:
    print(name[-1])

nums = [1,3,5,6,2]
total = 0

for num in nums:
    total += num
print(total)

items = ['Collin',2.5,[1,2,3],True,None,8]
print(len(items)) # there are 6 items in items :0

for thing in items:
    print(type(thing))

# count how many numeric values there are in the list of items

count = 0
for thing in items:
    if type(thing) == int or type(thing) == float:
        count += 1

print(count)

# building a list by using append

# list methods

names = ['Melinda','Chris','Collin','Andre']

# names  = names + 'Naomi' - This will not work - must append onto the end of the list

names.append("Naomi")
print(names)

print(names.append("Joe")) # the return value of the append method - which is None! - but it will still append Joe onto the end of the list

# using in and not in with lists
print("Chris" in names) # true
print("C" in names) # not true - not an individual list item

# Lists are mutable (Yay!!!!!!!!)

## don't do this:
# names = names.append("Billy") # deletes ur list! gives it None. What the hell.

names.append('Suzy')



