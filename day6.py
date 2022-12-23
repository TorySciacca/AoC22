"AoC Day 6 - Tory Sciacca"

data = open('day6.txt','r').read() #stores each line from the data in a variable 

def has_duplicate_chars(s): # Iterate over each character in the string
    for c in s: # Check if the (c)haracter appears more than once in the (s)tring
        if s.count(c) > 1:
            return True
    return False

for i in range(len(data)):#increment till 4 unique chars are found
    sequence = data[i:i+4] #creates 4 char sequence for each iteration
    if not has_duplicate_chars(sequence): #runs function
        print('Character\'s needed to be processed before the first start-of-packet marker is detected:',i+4)
        break
    i += 1 #continues if not found