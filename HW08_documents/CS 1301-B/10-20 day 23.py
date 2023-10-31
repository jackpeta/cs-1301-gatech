# 10-20 day 23 cs1301

# what percntaage of sacramento crime is bike related?
infile = open("day23police.csv","r")
headers = infile.readline() # str
datalines = infile.readlines() # list of str
infile.close()
count = 0
for line in datalines:
    pieces = line.split(",")
    district = pieces[1]
    offence = pieces[3]
    if "assault" in offence.lower() and district == '9':
        count += 1
# print(count)

newdict = {}
for line in datalines:
    pieces = line.split(",")
    district = pieces[1]
    offence = pieces[3]
    if district == " ":
        continue
    if "assault" in offence.lower():
        if district not in newdict:
            newdict[district] = 1
        else:
            newdict[district] += 1

f = open("day20limerick.txt","r")
text = f.read()
f.close()
text = text.replace("f","")
f2 = open("day20limerick.txt","w")
f2.write(text)
f.close()
print(text)
        
        
