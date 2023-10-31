# day 14 cs1301


alist = [1,2,3]
blist = alist # blist is an alias of alist - another name for the same variable
blist.append(999) # alist will also get the 999

clist = alist[:]

print(clist)

tupl = ("a",25)

# tuples can be indexed and sliced

print(tupl[0])
print(tupl[0:2]) # produces another tuple - subtuple?

# tupl[1] = 35 produces an error

alist = [1,2]
alist[0] = 999
print(alist) # works just fine i <3 lists

tup_a = ()
tup_b = (1,4,5)
tup_c = (9,) # need a comma to make it a tuple

print((4,5,6).count(4)) # counts the 4s in the tuple

print((4,5,6).index(6)) # find index of first 6

ta_list = [("Chris",10),("Priya",10),("Collin",9.999)]
ta_list.append(("Lasya",9.998))

# compute the average ranking for a ta

total = 0.0

for ta in ta_list:
    name = ta[0]
    ranking = ta[1]
    total += ranking

print(total / len(ta_list))

# OR

total = 0.0

for t(name,ranking) in ta_list:
    total += ranking

print(total / len(ta_list))

# if, as you went through the ta_list you needed to change something
# you couldn't do it easily - you would have to rebuild the tuple
    
