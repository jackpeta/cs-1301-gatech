import calendar

def bestMachine(machines,rating):

    highestRated = []
    i = 0
    max_rating = max(rating)
    print(max_rating)
          
    for machine in machines:
        tup = machine,rating[i]
        highestRated.append(tup)
        i += 1

    for tup in highestRated:
        if tup[1] < max_rating:
            highestRated.remove(tup)
            
    highestRated.sort()
    #print(highestRated)
                  
       
machines = ["Treadmill", "Stairs Machine", "Stationary Bike", "Leg Press"]
rating = [6.0, 5.7, 9.3, 9.3]
bestMachine(machines, rating)

def bulkOrder(foodCatalog):

    foodList = []
    totalCost = 0

    for foodName,price,protein in foodCatalog:
        if protein >= 20 and price < 8:
            totalCost += price
            foodList.append(foodName)

    foodsAndPrice = [foodList,totalCost]

    foodList.sort()

    return foodsAndPrice

bulkOrder([("Cookies", 2, 5), ("Steak", 7, 32), ("Beans", 2, 21),
("Chicken", 11, 35)])
[['Beans', 'Steak'], 9]

def organizeTimes(unorganizedTimeList):

    newTup = ()
    organizedTimeList = []
    i = 0

    for tup in unorganizedTimeList:
        tup[0].sort()
        organizedTimeList.append(tup[0][0:len(tup[0])-1]) # appends a new list, sorted, minus the last value

    for lists in organizedTimeList[:]:
         newTup = lists,unorganizedTimeList[i][0]
         organizedTimeList.append(newTup)
         i += 1
            
            

    #print(organizedTimeList)
                
            

unorganizedTimeList = [([7.05, 8.0, 6.2], "Andre"), ([6.14, 9.2, 7.2], "Collin"),
([7.42, 30.2, 6.34], "Ethan"), ([9.2, 8.1, 6.23], "Evan")]
organizeTimes(unorganizedTimeList)
[('Andre', [6.2, 7.05]), ('Collin', [6.14, 7.2]), ('Ethan', [6.34, 7.42]),
('Evan', [6.23, 8.1])]

def whenWaterslide(freeTime):

    for name, free_slots in freeTime:
        for free in free_slots:
            day = calendar.weekday(2023, free[0], free[1])
            if day in [0, 3, 4]:
                continue
            else:
                return False

        return True
            
freeTime = [("Collin", [(9, 19), (9, 20)]), ("Andre", [(9, 19)]),
("Ethan", [(9, 18), (9, 19)]), ("Evan", [(9, 20)])]
whenWaterslide(freeTime)


        
        

    
        
    
        

