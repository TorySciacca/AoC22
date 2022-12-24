"AoC Day 7 - Tory Sciacca"

data = open('day7.txt','r').read().split('\n') #stores each line from the data in a variable 
username = 'elf22'
dirs = []
path = ''

for command in data: #generate directory 
    
    if command[0] == '$': #function
        
        if command[2:4] == 'cd':
            
            if command[5] == '/': #return to main directory
                path += f'{username}/'

            if command[5:7] == '..': #move out a level
                pass
        
        elif command[2:4] == 'ls': #list command
            pass
    
    else: #directory or file

        if command[:3] == 'dir': #directory found
            # path += f'{command[3:]}'
            pass
            
        if command[0].isnumeric(): #file found
            pass
        
#test
print(path)

#process data
