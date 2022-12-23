"AoC Day 7 - Tory Sciacca"

data = open('day7.txt','r').read().split('\n') #stores each line from the data in a variable 

dirs = []
path = '/'

for command in data:
    
    if command[0] == '$':
        
        if command[3:4] == 'cd':
            pass
        
        elif command[3:4] == 'ls':
            pass
    
    else:
        pass
     
#     if l[0:4] == '$ cd':
#         directory_name = l[4:].strip()
#         print(directory_name)
#         ls = False
        
#     elif l[0:4] == '$ ls':
#         ls = True
        
#     if ls:
#         a = l.split(' ')
#         add_to_dir(directory_name,a[1],level)

#     i += 1
    
#     if i == 26:
#         break
    