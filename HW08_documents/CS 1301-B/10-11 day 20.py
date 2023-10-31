# 10/11 day 20 cs1301

# read the handout on try/except

try:
    print(blah)
    print(3/0)
except: # catches any runtime error
    print("an error happened")
finally: #optional, but always happens (even with return values)
    try:
        print(done)
    except:
        print("when handling finally a new error happened")

# open a file for reading

infile = open("day21limerick.txt", "r")

mytext = infile.read() #read whole thing as one giant str

print(mytext)

myline = infile.readline() # read some sort of line, every time you use it it reads the next line

infile.close()

print(myline)

infile = open("day21limerick.txt", "r")
line_list = infile.readlines()
infile.close()
print(line_list)
