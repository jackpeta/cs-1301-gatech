# hw06

def stayInSchool(people, networth, gender):

    stJudeList = []
    constanceBillardList = []

    for position,person in enumerate(people):
        if gender[position] == 'boy' and networth[position] >= 1:
            stJudeList.append(person)
        elif gender[position] == 'girl' and networth[position] >= 1:
            constanceBillardList.append(person)

    stJudeList.sort()
    constanceBillardList.sort()

    if len(stJudeList) >= 1 and len(constanceBillardList) == 0:
        return {'St. Jude': stJudeList}

    elif len(stJudeList) == 0 and len(constanceBillardList) >= 1:
        return {'Constance Billard': constanceBillardList}

    elif len(stJudeList) == 0 and len(constanceBillardList) == 0:
        return {}

    else:
        return {'St. Jude': stJudeList, 'Constance Billard': constanceBillardList}


def pearsonSpecterLitt(candidates):

    candidatesList = []
    gpaList = []

    for candidate, (gpa, school) in candidates.items():
        if school == 'Georgia Institute of Technology' or school == 'Georgia Tech':
            candidatesList.append(candidate)
            gpaList.append((gpa, candidate))  # append a tuple with GPA and candidate

    gpaList.sort(reverse=True)

    
    finalList = [candidate for gpa, candidate in gpaList]

    if finalList == []:
        print("Somebody find Mike Ross to fix this!")
        return []
    else:
        return finalList


def showFinder(showPreferences):
    watchDict = {}

    for person, shows in showPreferences.items():
        for show in shows:
            if show in watchDict:
                watchDict[show].append(person)
                watchDict[show].sort()
            else:
                watchDict[show] = [person]

    return watchDict


def chooseHouse(foodDict):

    familyList = []
    adjustedFamilyList = []
    counter = 0

    for family, food in foodDict.items():
        counter = 0
        for foodType, foodQuantity in food.items():
            if foodType == "turkey" or foodType == "gravy":
                counter += foodQuantity
                if counter > 10:
                    familyList.append(family)

    for item in familyList:
        if item not in adjustedFamilyList:
            adjustedFamilyList.append(item)

    adjustedFamilyList.sort()

    if adjustedFamilyList == []:
        return "No one has turkey and gravy?!?"
    elif len(adjustedFamilyList) == 1:
        return "Thanksgiving will be at {}!".format(adjustedFamilyList[0])
    elif len(adjustedFamilyList) == 2:
        return "Thanksgiving will be at {} or {}!".format(adjustedFamilyList[0],adjustedFamilyList[1])
    else:
        family_list_string = ", ".join(adjustedFamilyList[:-1])
        return "Thanksgiving will be at {}, or {}!".format(family_list_string, adjustedFamilyList[-1])
    

def bananaStand(menu, order):

    revenue = 0

    for item, quantity in order.items():
        if " - " in item:
            itemSplit = item.split(" - ")
            item_name = itemSplit[0]
            options = itemSplit[1].split(", ")
        else:
            item_name = item
            options = []

        price = 0

        if item_name in menu:
            price = menu[item_name]["price"]
            for option in options:
                if option in menu[item_name]:
                    price += menu[item_name][option]

        revenue += price * quantity

    return revenue
            
