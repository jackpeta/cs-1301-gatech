# code test

friendList = ["Collin","Caleb"]
candyList = [("Kit-Kat",5), ("Skittles",3.5)]

def chooseCandy(friendList, candyList):

    newdict = {}

    for index,friend in enumerate(friendList):
        candy,price = candyList[index]
        if price > 10:
                newdict[friend] = candy

    print(newdict)

chooseCandy(friendList, candyList)
        
