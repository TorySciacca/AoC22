"AoC Day 7 - Tory Sciacca"

data = open('day7.txt','r').read().split('\n') #stores each line from the data in a variable 
username = 'elf22'
dirs = []
path = 'username/'

for command in data: #generate directory 
    
    if command[0] == '$': #function
        
        if command[2:4] == 'cd':
            
            if command[5] == '/': #return to main directory
                path = 'username/'
                print(command)

            if command[5:7] == '..': #move out a level
                pass
        
        elif command[2:4] == 'ls':
            pass
    
    else: #directory or file

        if command[:3] == 'dir':
            pass
            
        if command[0].isnumeric():
            pass
        
#process data