# day 26 10-27 cs1301!

import requests

baseurl = "https://anapioficeandfire.com/api"
r = requests.get(baseurl)
print(type(r)) # response object - i can eiteher look at it as data or text
#data = r.json # converts text at that response into valid data if it's formatted correctly
data_dict = r.json()
#print(data_dict.keys())
houseurl = data_dict["houses"]
#sprint(type(newdata)) # it's a string! a new url...
r2 = requests.get(houseurl)
houselist = r2.json()

max_so_far = 0
max_house = ""
for house_dict in houselist:
    if len(house_dict["swornMembers"]) > max_so_far:
           max_so_far = len(house_dict["swornMembers"])
           max_house = house_dict["name"]
#print(max_house, max_so_far)

c_url = "https://anapioficeandfire.com/api/characters"
r3 = requests.get(c_url)
c_list = r3.json()
print(c_list[0])

