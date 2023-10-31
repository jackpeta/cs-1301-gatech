# day 22 notes - csv files

afile = open("day22alice.txt","a")
afile.write("\nThe END!!")
afile.close()

# if the file doesn't exist, it will be created

infile = open("day22crime.csv","r")
headers = infile.readline() # read the first line / header
data = infile.readlines() # read the data
infile.close

# print(data) # a list of str
# what is the average crime rate for these cities?

total = 0.0
for line in data:
    line = line.strip()
    pieces = line.split(",")
    total += float(pieces[-1]) #evrything in a file is a string!

print(total / len(data))
total = 0.0
sCount = 0
for line in data:
    line = line.strip()
    pieces = line.split(",")
    name = pieces[2]
    rating = float(pieces[3])
    if name[0] in "sS":
        sCount += 1
        total += rating

print(total / sCount)

# create a dictionary that maps each city name to its crime rating

newdict = {}

for line in data:
    line = line.strip()
    pieces = line.split(",")
    name = pieces[2]
    rating = float(pieces[3])
    newdict[name] = rating
print(newdict)




