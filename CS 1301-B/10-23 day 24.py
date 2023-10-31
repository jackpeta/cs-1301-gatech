# day 24 cs1301

# writing to a csv file

outfile = open("tainfo.csv","w")
outfile.write("name,role,salary\n")
outfile.write("Chris,head TA,12.50\n")
outfile.write("Collin,regular TA,9.50\n")
outfile.close()

# ^ creates a new file

# write three lists to a csv file called data.csv

headers = "name,role,salary\n"
names = ["Chris","Collin"]
roles = ["Head TA", "Regular TA"]
salaries = [12.5,9.5]

##outfile = open("data.csv","w")
##outfile.write(headers)
##for index in range(len(names)):
##    outfile.write(names[index] + "," + roles[index] + "," + "$" str(salaries[index]) + "\n")
##outfile.close()
                  
import requests
url = "https://pokeapi.co/api/v2/pokemon/3"
r = requests.get(url) # send a get request to this url
print(r) # prints ou the response
print(r.text[:500]) # r.text is a str
print(type(r.text))
