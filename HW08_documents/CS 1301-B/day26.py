# day 26 miniquiz


import requests

baseurl = "https://anapioficeandfire.com/api"
r = requests.get(baseurl)
data_dict = r.json()
bookurl = data_dict["books"]
r2 = requests.get(bookurl)
data = r2.json()

maxPageNumber = -1
biggestBook = ""

for bookDict in data:
    if bookDict['numberOfPages'] > maxPageNumber:
        maxPageNumber = bookDict['numberOfPages']
        biggestBook = bookDict['name']

return biggestBook

