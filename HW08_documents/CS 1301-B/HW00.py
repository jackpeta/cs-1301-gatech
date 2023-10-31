# practice problems

import auditionTools
import string

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

    weightedExam1Score = round(exam1Score * (10/100))
    weightedExam2Score = round(exam2Score * (15/100))
    weightedExam3Score = round(exam3Score * (15/100))

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

    return monthCounter

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

    fixedTicket = list(fixedTicket)
    return fixedTicket

def orderPlayers(playerList):

    newList = []
    orderedPlayerList = []

    for tup in playerList:
        tup = name,instrument,rawScore
        newtup = name, + instrument, + auditionTools.calculateScore(rawScore),
        newList.append(newtup)

    for position, tup in enumerate(newList):
        tup = name,instrument,newScore
        orderedPlayerList.insert(position, (name,newScore))

    for ch in orderedPlayerList:
        if ch not in string.ascii_letters:
            del ch

    print(orderedPlayerList)

playerList = [('Lee', 'Trumpet', [14,24,10]),
('Ethan', 'Flute', [20,41,9,10]),
('April', 'Trumpet', [0,0,12,21]),
('Kate', 'Saxophone', [31])]
orderPlayers(playerList)
['Ethan', 'Lee', 'Kate', 'April']


    
        
        

             


            

        

    


