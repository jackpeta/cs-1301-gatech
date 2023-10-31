"""
Georgia Institute of Technology - CS1301
Homework 7 - File I/O
"""

#########################################

"""
Function Name: inventoryManager()
Parameters: fileName (str)
Returns: organizedDict (dict)
"""

def inventoryManager(fileName):

    organizedDict = {}

    try:
        file = open(fileName, "r")
        header = file.readline()
        text = file.readlines()
        file.close()

        text = [item.strip('\n') for item in text] # strip all instances of newline for all items in the text

        nameList = []
        floatList = []
        intList = []
        storeOption = []

        for position,item in enumerate(text): # since the values are stored in a list with a pattern, we can use modulo to get the individual string in the repeating pattern
            if item == '':
                continue
            elif position % 5 == 1:
                nameList.append(item)
            elif position % 5 == 2:
                floatList.append(item)
            elif position % 5 == 3:
                intList.append(item)
            elif position % 5 == 4:
                storeOption.append(item)

        realFloatList = []

        realIntList = []

        for item in floatList:
            realItem = float(item)
            realFloatList.append(realItem)

        for item in intList:
            realItem = int(item)
            realIntList.append(realItem)

        for position,item in enumerate(nameList):
            if item not in organizedDict: 
                organizedDict[item] = []
                organizedDict[item].append(realFloatList[position])
                organizedDict[item].append(realIntList[position])
                organizedDict[item].append(storeOption[position])

        return organizedDict
                                           
    except FileNotFoundError:  
        return {}

inventoryManager("costumeStore1.txt")
    
    


#########################################

"""
Function Name: savvyShopper()
Parameters: fileName (str), shoppingMethod (str)
Returns: lowestPrice (tuple)
"""

def savvyShopper(fileName, shoppingMethod):
    if shoppingMethod == 'Online' or shoppingMethod == 'In-store':
        pass
    else:
        return ('', 0)

    try:
        masterDict = inventoryManager(fileName)

        lowestPrice = float('inf')  # anything below infinity will become the new lowest price
        lowestCostume = None  # assign none first then a costume corresponding to the relatively lowest price

        for key, value in masterDict.items():
            if shoppingMethod in value:
                price = value[0]
                if price < lowestPrice:
                    lowestPrice = price
                    lowestCostume = key

        if lowestCostume is not None:
            lowestPriceTup = (lowestCostume, lowestPrice)
            return lowestPriceTup
        else:
            return ('', 0)

    except FileNotFoundError:
        return ('', 0)

#########################################

"""
Function Name: costumePairs()
Parameters: totalBudget (int), shoppingMethod (str)
Returns: possiblePairs (list)
"""

def costumePairs(totalBudget, shoppingMethod):
    try:
        masterDict = inventoryManager("costumeStore1.txt")

        possibleCostumes = []
        possibleCostumePrices = []

        for costume, data in masterDict.items():
            price = data[0]
            method = data[2]
            if totalBudget >= price and method == shoppingMethod:
                possibleCostumes.append(costume) # accounts for correct shopping method
                possibleCostumePrices.append(price)

        possiblePairs = []

        for i in range(len(possibleCostumes)): # set 2 different indicing loops to avoid different paris
            for j in range(i + 1, len(possibleCostumes)):
                if possibleCostumePrices[i] + possibleCostumePrices[j] <= totalBudget:
                    costumeTup = (possibleCostumes[i], possibleCostumes[j])
                    costumeTup = sorted(costumeTup)
                    costumeTup = tuple(costumeTup)
                    possiblePairs.append(costumeTup)

        if len(possiblePairs) >= 1:
            return sorted(possiblePairs)
        else:
            return "No pairs of costumes can be purchased at this time."

    except FileNotFoundError:
        pass

costumePairs(60, 'In-store')



#########################################

"""
Function Name: logCandies()
Parameters: candyDict (dict)
Returns: None (NoneType)
"""

def logCandies(candyDict):

    total = 0

    infile = open("candylog.txt","w")
    infile.write("Candy Log\n")
    for key,value in candyDict.items():
        infile.write("\n")
        infile.write(key + "\n")
        infile.write(str(value) + "\n") # newlines account for formatting like in test case, sort of trial and error
        total += int(value)

    infile.write("\n")
    infile.write("Total Collected: {}".format(total))
    infile.close()
    
candyDict = {"Snickers": 10, "KitKat": 5, "Twizzlers": 8, "Trident": 7, "Extra": 3}
logCandies(candyDict)
    


#########################################

"""
Function Name: sortCostumes()
Parameters: fileName (str)
Returns: None (NoneType)
Raises: ValueError (Exception)
"""

def sortCostumes(fileName):
    infile = open(fileName, "r")
    outfile = open("sortedCostumeStore.txt", "w")
    text = infile.read()
    infile.close()

    if len(text) == 0:
        raise ValueError("An empty file was given. There is nothing to sort.")
    else:
        infile = open(fileName,"r")
        header = infile.readline().strip() # strip whitespace from top line
        masterdict = inventoryManager(fileName)

        costumeList = []
        priceList = []
        tupList = []

        for key, value in masterdict.items():
            costumeList.append(key)
            priceList.append(value[0]) # concerrent lists with same indice for key/value pair

        for i in range(len(costumeList)):
            newTup = (priceList[i], costumeList[i])
            tupList.append(newTup) # creates tuples from the two lists at the same indice

        tupList = sorted(tupList)
        
        outfile.write(header)

        for tup in tupList:
            costume = tup[1]
            price = tup[0]

            outfile.write("\n" + "\n" + costume + "\n" + str(price) + "\n" + str(masterdict[costume][1]) + "\n" + str(masterdict[costume][2]))

        infile.close()
        outfile.close()

sortCostumes('costumeStoreShort.txt')



#########################################
