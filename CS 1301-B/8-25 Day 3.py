# day 3 8/25/23

##value = 3
##print(value)
##
##print(type(value))
##new_value = int(value)
##print(new_value)


# Functions

##def Welcome():
##    name = input("Enter restaurant name: ")
##    print("Welcome to " + name)
##
####Welcome()
##
##def pizza_cost():
##    Welcome()
##    crustcost = 4.00
##    ingredientcost = 2.25
##    numingredients = input("How many toppings? ")
##    total_cost = crustcost + (ingredientcost * int(numingredients))
##    print("Your total cost is: $" + str(total_cost))
##
##pizza_cost()

# integer divisiom

##carton_size = 12
##num_eggs = 5233
##
##print(num_eggs / carton_size)

def how_many_nickels(num_dollars):
    pennies = num_dollars * 100
    nickels = pennies // 5
    leftover = pennies % 5
    print("Nickels: " + str(nickels))
    print("Pennies: " + str(leftover))
    


how_many_nickels(.5)
how_many_nickels(1.25)

