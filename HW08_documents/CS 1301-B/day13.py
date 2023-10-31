# day13.py 


def every_other(list):
    list = list[::2]
    newList = []
    for item in list:
        if type(item) == str:
          newList.append(item)

    return newList
