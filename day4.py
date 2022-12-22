"AoC Day 4 - Tory Sciacca"

total_overlaps = 0
data = open('day4.txt','r').read().splitlines() #stores each line from the data in a variable 

for i in data: #iterate each line
    a,b = i.split(',') #seperate each elf sections elf a and elf b
    aa,aaa = [int(x) for x in a.split("-")] #aa = first section, aaa = last
    bb,bbb = [int(x) for x in b.split("-")] #""
    
    if (aa <= bb and aaa >= bbb ) or (bb<=aa and bbb>=aaa): #only increment if either section can fit entierly within the other
        total_overlaps += 1
                
print(f'The number of total overlaps is: {total_overlaps}') #result