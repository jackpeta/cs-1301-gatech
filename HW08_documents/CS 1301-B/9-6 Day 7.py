# day 7 CS 1301

num = 1
while num <= 5:
    print(num)
    num += 1

# num % 2 == 0 (this is a way to verify if the number is even - divided by 2 with no remainder

for letter in "jackets":
    print(letter)

    #if the thing you are looping through is a string, it will get out each piece of the string(Which is a character)

for letter in "123":
    print(letter)

##name = input("Enter your name ")
##while name != "Jack":
##    print("go away!")
##    name = input("Re-enter your name ")

for value in [1,2,3]:
    print(value)

# if you wantn umbers from 1 to 25, you can get the pieces in a function called range

for number in range(1,25):
    print(number)
# will only take me to 24, because range always stops 1 before the end, and only give integers

print("          ")

for num in range(3):
    print(num)

    # if only 1 number, it is the "stop" with the default start being 0.

for num in range(2,8,2):
    print(num)

    #goes in steps of 2 but will never hit 8

print("                          ")

def how_many_vowels(sentence):

    count = 0

    for letter in sentence:
        if letter in "aeiouAEIOU":
            count += 1
    print(count)

how_many_vowels("Hello everyone!")


