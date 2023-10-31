"""
Georgia Institute of Technology - CS1301
Homework 8 - CSV Files/APIs
"""

import requests

#########################################

"""
Function Name: newRecruits()
Parameters: movieNum (int)
Returns: winner (str)
"""

def newRecruits(movieNum):

    infile = open("starWars.csv","r")
    header = infile.readline()
    data = infile.readlines() # extract data
    infile.close()

    data = [item.strip('\n') for item in data]
    data = [item.split(',') for item in data] # get rid of newline and split the lists into sublists via comma separation

    masterdict = {} # gonna do a dictionary sorta like hw07... hopefully useful later?
    for item in data:
        character = item[0]
        midiCount = int(item[1])
        species = item[2]
        movieNumber = int(item[3])
        if character not in masterdict:
            masterdict[character] = [midiCount, species, movieNumber]

    jediCount = 0 # separate counts to keep track of midi counts per jedi/sith
    sithCount = 0

    for character,values in masterdict.items():
        if values[2] == movieNum:
            if int(values[0]) > 0:
                jediCount += values[0] # stored in list as str so must convert to int to add to total
            else:
                sithCount += abs(values[0])

    if jediCount == 0 and sithCount == 0:
        return "No new recruits!"
    elif jediCount > sithCount:
        return "The Jedis have won by {} points!".format(jediCount - sithCount)
    else:
        return "Oh no, the Siths are better!"    


#########################################

"""
Function Name: orgByType()
Parameters: minChlorians (float), maxChlorians (float)
Returns: organizedDict (dict)
"""

def orgByType(minChlorians, maxChlorians):

    infile = open("starWars.csv","r")
    header = infile.readline()
    data = infile.readlines() # extract data
    infile.close()

    data = [item.strip('\n') for item in data]
    data = [item.split(',') for item in data] # get rid of newline and split the lists into sublists via comma separation

    masterdict = {} # gonna do a dictionary sorta like hw07 problem 1
    for item in data:
        character = item[0]
        midiCount = int(item[1])
        species = item[2]
        movieNumber = int(item[3])
        if character not in masterdict:
            masterdict[character] = [midiCount, species, movieNumber]

    # ^ all work from problem 1 - copy/paste code instead of function call because function doesnt return a dict

    characterTypeDict = {}
    for key,value in masterdict.items():
        if value[1] not in characterTypeDict:
            characterType = value[1]
            characterTypeDict[characterType] = [[key, value[0]]] # making it a sublist instead of a list because i want to index individual characters under their type
        elif value[1] in characterTypeDict:
            characterType = value[1]
            characterTypeDict[characterType].append([key, value[0]]) # covers the case where there are multiple characters of same species/type

    organizedDict = {}
    for key,value in characterTypeDict.items():
        for sublist in value:
            if key not in organizedDict and minChlorians <= sublist[1] <= maxChlorians: # min/max is inclusive
                organizedDict[key] = [sublist[0]]
            elif key in organizedDict and minChlorians <= sublist[1] <= maxChlorians:
                organizedDict[key].append(sublist[0]) #append for all characters of same species that satisfy logic
            else:
                continue

    for key,value in organizedDict.items():
        value = sorted(value)
        organizedDict[key] = value # re-assign the value as the alphabetically sorted list

    if len(organizedDict) == 0:
        return {} # covers empty species names with no characters that satisfy logic - we append species name before going through logic
    else:
        return organizedDict
    
#########################################

"""
Function Name: possiblePlanets()
Parameters: favPlanets (list)
Returns: destinationDict (dict)
"""

def possiblePlanets(favPlanets):

    baseUrl = "https://swapi.dev/api/planets/?search="
    destinationDict = {}

    for planet in favPlanets:
        try:
            r = requests.get(baseUrl + planet)
            if r.status_code == 200: # if the website is up
                data = r.json()
                if "results" in data:
                    planets_data = data["results"] # results should always be in data but Whatever
                    for planet_data in planets_data:
                        name = planet_data.get("name")
                        climate = planet_data.get("climate")
                        if 'temperate' in climate: # looks through climate for temperate
                            destinationDict[name] = climate    # appends all of climate including temperate, but other things as well
        except:
            continue

    if len(destinationDict) == 0: # does the dictionary have at least 1 key/value pair
        return {}
    else:
        return destinationDict

#########################################

"""
Function Name: residentHeights()
Parameters: planet (str)
Returns: heights (list)
"""
def residentHeights(planet):
    baseUrl = "https://swapi.dev/api/planets/?search="
    heights = []

    try:
        r = requests.get(baseUrl + planet)
        if r.status_code == 200: # if its up
            data = r.json()
            if "results" in data:
                planets_data = data["results"]
                for planet_data in planets_data:
                    residents = planet_data.get("residents")
                    for website in residents: # residents generates a list containing websites corresponding to planet inhabitants, so i have to parse that too
                        r = requests.get(website)
                        character_data = r.json()  
                        height = character_data.get("height")
                        name = character_data.get("name")
                        characterTup = (int(height), name) # stored as a str for some reason in the json
                        heights.append(characterTup)
        heights = sorted(heights) # sorts by height in the returned list
        return heights
    except:
        return []

#########################################

"""
Function Name: starshipInfo()
Parameters: starships (list)
Returns: None (NoneType)
"""

def starshipInfo(starships):
    infile = open("starships.csv", "w")
    infile.write("Starship Name,Model,Starship Class,Passengers")
    
    base_url = "https://swapi.dev/api/starships/?search="

    for starship in starships:
        try:
            url = base_url + starship.replace(" ", "+") # THIS TOOK ME LIKE AN HOUR TO DEBUG YOU NEED THE + SPECIFICALLY I HATE IT HERE
            r = requests.get(url)

            if r.status_code == 200: # if the website is valid and up
                data = r.json()
                starships_data = data.get("results") # formatting from the json

                if starships_data:
                    for starship_data in starships_data:
                        name = starship_data.get("name") # indexing the individual characteristics from the API
                        model = starship_data.get("model")
                        starship_class = starship_data.get("starship_class")
                        passengers = starship_data.get("passengers")

                        infile.write("\n{},{},{},{}".format(name, model, starship_class, passengers))
                else:
                    print(f"No results for starship: {starship}")
            else:
                print(f"Request to SWAPI failed for starship: {starship}")
        except:
            print("An error occurred for starship: {starship}")

    infile.close()

#########################################
