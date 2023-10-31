#########################################
"""
Function Name: chickenAndEggs()
Parameters: numDays (int), numEggs (int), numChicken (int),
mealsOutside (int)
Returns: isExpired (bool)
"""

def chickenAndEggs(numDays, numEggs, numChicken, mealsOutside):
    
    mealsInADay = numDays * 3 
    eggMeals = numEggs * 4 
    chickenMeals = numChicken * 2 
    outsideMeals = mealsOutside * 1 

    numMeals = eggMeals + chickenMeals + outsideMeals

    print(numMeals)

    if numMeals > (numDays * 3):
        return False
    elif numMeals <= (numDays * 3):
        return True
    else:
        return 'Error'

    
#########################################
"""
Function Name: enterTheCave()
Parameters: phrase (str), code (int)
Returns: None (NoneType)
"""
def enterTheCave(phrase, code):

    phrase = str(phrase)
    code = int(code)

    if phrase == "Open Sesame" and code <= 25:
        print("You have opened the door")

    elif phrase == "Hello World" and 75 <= code <= 100:
        print("You have opened the door")

    elif phrase == "Python Enjoyer" and code == 50:
        print ("You have closed the door")

    else:
        print ("INTRUDER ALERT")        
    
#########################################
"""
Function Name: jackAndJill()
Parameters: jackHeight (int), jillHeight (int), jamesHeight (int),
direction (str)
Returns: personInFront (str)
"""
def jackAndJill(jackHeight, jillHeight, jamesHeight, direction):

    jackHeight = int(jackHeight)
    jillHeight = int(jillHeight)
    jamesHeight = int(jamesHeight)
    direction = str(direction)

    if jackHeight > jillHeight and jackHeight > jamesHeight and direction == 'downhill':
        return 'Jack needs to be in front.'

    elif jillHeight > jamesHeight and jackHeight > jamesHeight and direction == 'uphill':
        return 'James needs to be in front.'

    elif jillHeight > jamesHeight and jillHeight > jackHeight and direction == 'downhill':
        return 'Jill needs to be in front.'

    elif jamesHeight > jackHeight and jamesHeight > jillHeight and direction == 'downhill':
        return 'James needs to be in front.'

    elif  jackHeight > jillHeight and jamesHeight > jillHeight and direction == 'uphill':
        return 'Jill needs to be in front.'

    elif jillHeight > jackHeight and jamesHeight > jackHeight and direction == 'uphill':
        return 'Jack needs to be in front.'

    else:
        return "Error - Debug me"

#########################################
"""
Function Name: closestShip()
Parameters: currentPosition (int)
Returns: None (NoneType)
"""
def closestShip(currentPosition):

    currentPosition = int(currentPosition)

    dutchmanPosition = abs(currentPosition - 175)

    pengPosition = abs(currentPosition - 320) 

    pearlPosition = abs(currentPosition - 515)

    if dutchmanPosition < pengPosition < pearlPosition or dutchmanPosition < pearlPosition < pengPosition:
        print("The Flying Dutchman")

    elif pengPosition < dutchmanPosition < pearlPosition or pengPosition < pearlPosition < dutchmanPosition:
        print("Hai Peng")

    elif pearlPosition < dutchmanPosition < pengPosition or pearlPosition < pengPosition < dutchmanPosition:
        print("The Black Pearl")

    else:
        print("Error - debug me")
    
#########################################
"""
Function Name: wizardOfOz()
Parameters: maxDistance (int), maxHostility (float)
Returns: locationToVisit (str)
"""
def wizardOfOz(maxDistance, maxHostility):

    maxDistance = int(maxDistance)
    maxHostility = float(maxHostility)

    if 0 <= maxDistance < 200 or 0.0 <= maxHostility < 1.0:
        return "Dorothy must go back to Kansas."

    elif maxDistance >= 200 and 9.0 <= maxHostility:
        return "Deadly Desert"

    elif maxDistance >= 600 and 7.0 <= maxHostility:
        return "Munchkin Country"

    elif maxDistance >= 1000 and 5.0 <= maxHostility:
        return "Winkie Country"

    elif maxDistance >= 1500 and 1.0 <= maxHostility:
        return "Emerald City"

    else:
        return "Dorothy must go back to Kansas."


#########################################
