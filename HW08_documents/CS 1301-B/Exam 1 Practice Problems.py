# practice problems

def schoolSupplies():

    penNumber = int(input("How many pens do you want? "))
    notebookNumber = int(input("How many notebooks do you want? "))
    folderNumber = int(input("How many folders do you want? "))

    totalCost = (.5 * penNumber) + (5 * notebookNumber) + (3 * folderNumber)

    print("You need to spend ${} on school supplies.".format(totalCost))


def gradeCalculator():

    exam1Score = float(input("What was your Exam 1 score? "))
    exam2Score = float(input("What was your Exam 2 score? "))
    exam3Score = float(input("What was your Exam 3 score? "))

    weightedExam1Score = exam1Score * (10/100)
    weightedExam2Score = exam2Score * (15/100)
    weightedExam3Score = exam3Score * (15/100)

    cumulativeScore = weightedExam1Score + weightedExam2Score + weightedExam3Score + 5 + 35

    neededScore = (90 - cumulativeScore) * 5

    print("You need a {}% on the final to get an A.".format(neededScore))

def closestStore(userLocation):

    userLocation = int(userLocation)

    barnesNobleDistance = abs(5 - userLocation)
    amazonDistance = abs(3 - userLocation)
    publixDistance = abs(2 - userLocation)
    targetDistance = abs(8 - userLocation)

    if barnesNobleDistance < amazonDistance and barnesNobleDistance < publixDistance and barnesNobleDistance < targetDistance:
        print('Barnes & Noble')

    elif amazonDistance < barnesNobleDistance and amazonDistance < publixDistance and amazonDistance < publixDistance:
        print('Amazon')

    elif publixDistance < barnesNobleDistance and publixDistance < amazonDistance and publixDistance < targetDistance:
        print('Publix')

    elif targetDistance < barnesNobleDistance and targetDistance < amazonDistance and targetDistance < publixDistance:
        print('Target')

    elif publixDistance == barnesNobleDistance or publixDistance == amazonDistance or publixDistance == targetDistance:
        print('Publix')

    elif amazonDistance == barnesNobleDistance or amazonDistance == targetDistance:
        print('Amazon')

    elif barnesNobleDistance == targetDistance:
        print('Barnes & Noble')

def growFollowing(currentFollowing,goal):

    monthCounter = 0
    while currentFollowing < goal:
        monthCounter += 1
        currentFollowing += 5000

    print(monthCounter)

def playoffs(team1name,team2name,scoreCount):

    team1Score = 0
    team2Score = 0
    
    for ch in scoreCount:
        if ch in ('1'):
            team1Score += 1
        elif ch in ('2'):
            team2Score +=1

    if team1Score > team2Score:
        winningTeam = ("{} has won the game!".format(team1name))
        return winningTeam

    elif team2Score > team1Score:
        winningTeam = ("{} has won the game!".format(team2name))
        return winningTeam

    elif team2Score == team1Score:
        winningTeam = "It was a tie :("
        return winningTeam

def fixTickets(ticketNumber):

    fixedTicket = ''
    for x in ticketNumber:
        if x.isupper() == True:
            x = x.lower()
            fixedTicket += x
        elif x.islower() == True:
            x = x.upper()
            fixedTicket += x
        elif x.isdigit() == True:
            fixedTicket += x

    return fixedTicket


            

        

    


