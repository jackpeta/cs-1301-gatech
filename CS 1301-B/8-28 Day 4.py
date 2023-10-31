# CS1301 8/28 DAy 4!


def say_hello(name,age):
    print("Hello {} year old {}!".format(age, name))

say_hello("Jack",18)
say_hello("Fart",17)
say_hello("Balls",19)

name= "Joe"
age = str(6)

##say_hello(age,name)

def square_area(side):
    return side ** 2


def hyphenate(astr):
    return astr + "-" + astr

new_word = hyphenate("cat")
print(new_word)

new_new_word = hyphenate(new_word)
print(new_new_word)

##new_word = hyphenate(3) won't work!!!
##print(new_word)
                     
# compute average of 3 graces where the first one counts twice as much as the other two grades

def calc_average(int1,int2,int3):
    return ((2 * int1) + int2 + int3) / 3

average = calc_average(10,20,30)
print(average)



    

