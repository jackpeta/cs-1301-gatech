# 10-30 day 27

def blastoff(num):
    if num == 0:
        print("BLASTOFF!")
    else:
        print(num)
        blastoff(num - 1)

#blastoff(20)

# sum up the numbers from 0 to the input parameter

def sum_up(num):
    if num == 0:
        return 0 # we know the sum of the numbers from 0 to 0
    return num + sum_up(num - 1)

#print(sum_up(4))

# sum up the values in a list using recursion

def sum_list(alist):
    if alist == []:
        return 0
    else:
        return alist[0] + sum_list(alist[1:]) # add the first item then call the function with a smaller list as the param
        




print(sum_list([4,2,1]))
