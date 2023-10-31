# 10-25 day 25 cs1301

import requests

##baseurl = "http://pokeapi.co/api/v2/"
##parturl = "pokemon/charmander/"
##r = requests.get(baseurl + parturl)
##print(r) # prints the status code - 200 is good 404 is not good
##print(r.text[0:500])
##data = r.json() # convert str to appropriate data typee
##
### what if the website works but is html not json? what will happen
##
##r = requests.get("https://www.gatech.edu")
##print(r)
###page = r.json() doesnt work bc its html
##print(r.text[:1000])
##
##baseurl = "https://swapi.dev/api/"
##parturl = "/people/1"
##r = requests.get(baseurl + parturl)
##print(r)
##data = r.json()
##print(type(data))
##print(data.keys())
##name = data["name"]
##newurl = data["homeworld"]
##r2 = requests.get(newurl)
##print(r2)
##data2 = r2.json()
##print(data2.keys)
##planet = data2["name"]
##print(planet)

r = requests.get("https://anapioficeandfire.com/api")
data = r.json()
r2 = requests.get(data['houses'])
data = r2.json()
print(data[0]['swornMembers'])
