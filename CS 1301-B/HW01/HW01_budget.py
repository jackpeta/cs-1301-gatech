##Description: As a new college student, it's important to get a handle on budgeting your monthly in-
##come so you can stay on top of your spending. Write a function called budget() that asks the user
##for their monthly income and what percentage of the monthly income the user wants to save. After
##putting the savings portion of the income in a savings account, deduct required monthly spendings,
##including housing ($700 per month) and food ($50 per week). The function should then print out the
##amount of money saved per month, and the amount of money left in the budget to spend
##elsewhere.
##Note: You can assume there are 4 weeks in a month. Round all outputs to two decimal places.
##Hint: Do not assume that all inputs will be integers.
##>>> budget()
##What is your monthly income? 1200
##What percentage of your income do you want to save? 25
##You can save $300.0 and spend $0.0 this month.
##>>> budget()
##What is your monthly income? 1600
##What percentage of your income do you want to save? 10
##You can save $160.0 and spend $540.0 this month.

##def budget():
##
##    monthlyincome = input('What is your monthly income? ')
##
##    monthlyincome = int(monthlyincome)
##
##    monthlysave = input('What percentage of your income do you want to save?' )
##
##    monthlysave = int(monthlysave)
##
##    save = (monthlyincome * (monthlysave / 100))
##
##    spend = monthlyincome - save - 900
##
##    print("You can save ${} and spend ${} this month." .format(save, spend))
##    
##
##budget()

def budget():

    monthlyincome = int(input('What is your monthly income? '))

    monthlypercentsaved = int(input('What percentage of your income do you want to save? '))

    realincome = int(monthlyincome - 900)

    monthlysaved = (monthlyincome * (monthlypercentsaved / 100))

    monthlyspend = realincome - monthlysaved

    print("You can save ${} and spend ${} this month." .format(monthlysaved, monthlyspend))

budget()

    
