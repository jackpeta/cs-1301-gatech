#########################################

def reviveSecretMessage(corruptedMessage):

    if "(" or "#" or "%" in corruptedMessage:
        corruptedMessage = corruptedMessage.replace("(","") 
        corruptedMessage = corruptedMessage.replace("#","")
        corruptedMessage = corruptedMessage.replace("%","")

        revivedMessage = corruptedMessage
        return revivedMessage
    else:
        revivedMessage = corruptedMessage
        return revivedMessage

def crackCode(code1, code2):

    reversedCode1 = list(reversed(code1))
    reversedCode2 = list(reversed(code2))

    #append the characters in list form! 

    common_characters = []
    for x in range(len(reversedCode1)):
        if reversedCode1[x] == reversedCode2[x]:
            common_characters.append(reversedCode1[x])

    message = ''.join(common_characters)
    return message

def calculateDistance(operations, initialNumber):
    operations = list(operations)
    initialNumber = int(initialNumber)

    while initialNumber <= 30 and operations:
        for ch in operations:
            if ch == "*":
                initialNumber = initialNumber * 3
            elif ch == "/":
                initialNumber = initialNumber // 2
            elif ch == "+":
                initialNumber = initialNumber + 7
            elif ch == "-":
                initialNumber = initialNumber - 4

    if initialNumber >= 31:
        lowerDistance = initialNumber
        return lowerDistance

def escapeThumbs(numberOfThumbs, obstacles):

    numberOfThumbs = int(numberOfThumbs)
    obstacles = str(obstacles)

    numObstacles = 1
    for ch in obstacles:
        if ch in ",":
            numObstacles += 1

    numThumbsLeft = numberOfThumbs - numObstacles
        
    if numberOfThumbs > numObstacles:
        return "Mission failed: {} still following!".format(numThumbsLeft)
    if numberOfThumbs <= numObstacles:
        return "Success! You've escaped!"

def timeLeft(puzzleTimes, minutesLeft):
    puzzleTimes = str(puzzleTimes)
    minutesLeft = int(minutesLeft)
    puzzleValue = 0

    for ch in range(0, len(puzzleTimes), 2):
        puzzleSliced = puzzleTimes[ch:ch + 2]
        puzzleValue += 2 * int(puzzleSliced)

    time_remaining = minutesLeft - puzzleValue

    if time_remaining >= 0:
        return "You have {} minutes left over!".format(time_remaining)
    else:
        return "London is doomed..."

    

    

    
        

    




    

