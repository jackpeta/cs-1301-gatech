# day23.py

def file_stuff(infile, outfile):
    with open(infile, "r") as x:
        text = x.read()

    cleaned_text = text.replace(",", "").replace("'", "").replace("!", "")
    words = cleaned_text.split()

    with open(outfile, "w") as y:
        for word in words:
            y.write(word + '\n')

file_stuff("day23_poem.txt", "day23_words.txt")







            
            
