# day 19 10-6

# print(3/0) gives a ZeroDivisionError

num = 0
if num != 0:
    print(3/num)
else:
    print("undefined")

# catch a zero division error

try:
    print(3/num)
except ZeroDivisionError:
    print("undefined")
except:
    print("an error occurred")

# key error

adict = {3:8}

try: #try to run the whole block of code nested within the try
    print(3/num)
    print(adict[num])
except ZeroDivisionError: #catch divide by zero
    print("Undefined")
except: #catch any kind of error
    print("An error occurred")

##
##alist = [3,4,5,.6,0,10]
##try:
##    for item in alist:
##        print(100/item)
##    except:
##        print("oops")

# or

try:
    for item in alist:
        print(100/item)
except:
    print("oops")

# the above code stops when you hit zero

# write a function called raise_price that takes 3 param
# a dictionary of items and prices
# a list of items that need the price to be raised
# a factor to raise the price by
# if the item is not in the dictionary put it in there with price 0


def raise_price(adict,alist,factor):
    for item in raising_list:
        if item in adict:
            adict[item] = adict[item] * (1.0 + factor/100)
        else:
            adict[item] = 0.0
        adict[item] = round(adict[item],1)
        


price_dict = {"wand":2.5, "robe":4.0, "broom":6.0}
raising_list = ["robe","broom"]
factor = 10






