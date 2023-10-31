def teamwork(hero1,hero2):
    counter = 0

    for i in range(0, len(hero1)):
        if hero1[i] == hero2[i]:
            counter += 1

    print(counter)

def countOrders(orders):
    b = 0
    f = 0
    s = 0

    for ch in orders:
        if ch == 'b':
            b +=1
        elif ch == 'f':
            f+=1
        elif ch == 's':
            s+=1

    if b > s and b > f:
        print("burger")

    if s > b and s > f:
        print("soda")

    else:
        print("fries")

def findLunchPrice(prices):
    costCounter = 0

    for ch in prices:
        if ch.isdigit() == True:
            ch = int(ch)
            costCounter += ch

    if costCounter != 0:
        print("Your lunch cost {}".format(costCounter))

    else:
        print("free lunch")
        
