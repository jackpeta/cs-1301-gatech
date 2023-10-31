"""
Georgia Institute of Technology - CS1301
Homework 01 - Functions & Expressions
"""
#########################################

def ratsNightTrivia():
    
    answer1 = input("What is the name of Georgia Tech's fight song? ")

    print("You answered:",answer1)
    
    print("The right answer is: Ramblin' Wreck from Georgia Tech")

    print("")
    
    answer2 = input("What's the good word?")
                   
    print("You answered:",answer2)
                   
    print("The right answer is: To hell with georgia")
    

def rockRambleRoll():
    pizza_answer = input('How many pizzas do you want at Campus Crust? ')
    sandwich_answer = input('How many sandwiches do you want at 5th Street Deli? ')
    sushi_answer = input('How many sushi rolls do you want at Bento Sushi? ')
    taco_answer = input('How many tacos do you want at Twisted Taco? ')


    pizza_answer = int(pizza_answer)
    sandwich_answer = int(sandwich_answer)
    sushi_answer = int(sushi_answer) 
    taco_answer = int(taco_answer)


# trying to convert all answers to integers because of weird errors

    total_cost = ((pizza_answer * 9.0) + (sandwich_answer * 5.5) + (sushi_answer * 8.0) + (taco_answer * 2.25))


    print("You need to spend ${} at Rock, Ramble, and Roll." .format(total_cost))

rockRambleRoll()

def houseParty():

    autograph_answer = input('How many autographs will you get? ')
    bouncy_castle_answer = input('How many times will you visit the bouncy castle? ')
    video_game_answer = input('How many video game contests will you participate in? ')
    locker_room_answer = input('How many times will you walk through the locker rooms? ')

#made answers into integers to avoid errors

    autograph_answer = int(autograph_answer)
    bouncy_castle_answer = int(bouncy_castle_answer)
    video_game_answer = int(video_game_answer)
    locker_room_answer = int(locker_room_answer)

    hours = (((autograph_answer * 10) + (bouncy_castle_answer * 20) + (video_game_answer * 45) + (locker_room_answer * 15)) // 60)

    minutes = ((autograph_answer * 10) + (bouncy_castle_answer * 20) + (video_game_answer * 45) + (locker_room_answer * 15)) % 60

# need the remainder and i didnt know what % was so this took me so long

    print('You will spend {} hour(s) and {} minutes at the house party.' .format(hours, minutes))

houseParty()

def budget():

    monthlyincome = int(input('What is your monthly income? '))

    monthlypercentsaved = int(input('What percentage of your income do you want to save? '))

    realincome = int(monthlyincome - 900)

    monthlysaved = (monthlyincome * (monthlypercentsaved / 100))

    monthlyspend = realincome - monthlysaved

    print("You can save ${} and spend ${} this month." .format(monthlysaved, monthlyspend))

budget()

    
def spareTime():

    credit_hours = input('How many credit hours are you taking? ')

    credit_hours = int(credit_hours)

    extra_hours = input('How many hours will you devote to extracurricular activities each day? ')

    extra_hours = int(extra_hours)

    spare_hours = (112 - (credit_hours * 4) - (extra_hours * 7))

    daily_spare_hours = (spare_hours / 7)

# ^ more accurate for calculation, but can't have a decimal hour in the final product

    daily_spare_minutes = ((daily_spare_hours * 60) % 60)

    daily_spare_hours = (spare_hours // 7)

# ^ converting it back to an integer for display purposes

    daily_spare_minutes = round(daily_spare_minutes, 1)

    print('You have {} hour(s) and {} minutes per day to spare.' .format(daily_spare_hours, daily_spare_minutes))
   
spareTime()



    

    
    
    



    
