def makeChange(total, payment):

    total = float(total)
    payment = str(payment)

    paymentFloat = 0

    for ch in payment:
        if ch == 'd':
            paymentFloat += 1
        elif ch == 'q':
            paymentFloat += .25
        elif ch == 'n':
            paymentFloat += .05

    changeAmount = paymentFloat - total

    changeAmount = round(changeAmount,2)

    return "${} is your change.".format(changeAmount)

def prepareFood(orders):
    orders = orders.lower()

    if orders == '':
        return []
    
    ordersList = orders.split('*')
    
    newOrdersList = []

    for item in ordersList:
        cleaned_order = ""
        for ch in item:
            if ch.isalpha():
                cleaned_order += ch
        
        newOrdersList.append(cleaned_order)

    fixedOrdersList = []
    
    for item in newOrdersList:
        if item[0] not in 'bo':
            fixedOrdersList.append(item)
        elif item[0] == 'b':
            fixedOrdersList.append(item[1:])
            fixedOrdersList.append(item[1:])
        elif item[0] == 'o':
            continue

    fixedOrdersList.sort()

    return fixedOrdersList
    
def drivingTest(rubric, actions):
    score = 0

    for action in actions:
        for sublist in rubric:
            if action == sublist[0]:
                score += sublist[1]

    if score < 200:
        return "With a score of {}, SpongeBob has failed once again!".format(score)
    else:
        return "With a score of {}, SpongeBob has passed his driving test!".format(score)


def musicalNight(potentialMembers, membersInstruments, squidwardInstruments):

    bandMembers = []

    for instrument in squidwardInstruments:
        if instrument in membersInstruments:
            instrumentIndex = membersInstruments.index(instrument)
            bandMembers.append(potentialMembers[instrumentIndex])

    bandMembers.sort()

    if bandMembers == []:
        print("I guess it's just me and you Clarry : /")
        return []

    else:
        return bandMembers

def dayOut(spongebobFavorites, friends, friendsFavorites):
    friendsToHangout = []

    for i in range(len(friends)):
        friend = friends[i]
        common_places = []
        for place in spongebobFavorites:
            if place in friendsFavorites[i]:
                common_places.append(place)
        if len(common_places) >= 2:
            friendsToHangout.append(friend)

    friendsToHangout.sort()

    if not friendsToHangout:
        print("It's just a day of fine dining and breathing")
        return []

    return friendsToHangout










            
        
        
                
                        
            






    


