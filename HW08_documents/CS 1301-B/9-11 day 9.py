# Day 9 CS 1301

for num in range(100):
    print(num)
    break
print("after loop")

for num in range(100):
    print(num)
    if num > 4:
        break #exit loop
print("after loop")

print("                 ")

for num in range(10):
    print(num)
    if num > 2 and num < 5:
        continue # go back up - do not print the squared version
    print(num**2)

for num in range(-3,3):
    print(num)
    if num == 0:
        continue # do not continue the code that follows this, get a new number (avoids division by zero error)
    print(10/num)
# keeping a running total - continue to buy things at a store until i run out of money or have bought 5 things
##money_spent = 0.0
##for count in range(0,5): # count in range(0,5) is a good way to say - repeat this 5 times (smart!)
##   # cost = float(input("cost of the item: "))
##    if money_spent + cost > 10.0:
##        break
##    money_spent += cost

print("you spent ${}".format(money_spent))

for num in range(3):
    for num2 in range(2):
        print(num2)
        break

    # this will print 3 0s because the break satement exits out of the loop immediately





    
