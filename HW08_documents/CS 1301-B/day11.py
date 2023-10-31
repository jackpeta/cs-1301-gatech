def count_it(anint):

    anint = str(anint)

    counter = 0

    for ch in anint:
        ch = int(ch)
        if ch % 2 == 0:
            counter += 1

    return counter

        
