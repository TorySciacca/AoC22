"AoC Day 7 - Tory Sciacca"

data = open('day7.txt','r').read().split('\n') #stores each line from the data in a variable 
username = 'elf22'
dirs = ['/',[]]
path = ''
level = 1

for command in data: #generate directory 
    
    if command[0] == '$': #function
        
        if command[2:4] == 'cd':
            
            if command[5] == '/': #return to main directory
                path += f'{username}/'

            elif command[5:7] == '..': #move out a level
                pass
            
            else: 
                for i in dirs[level]:
                    if i == command[4:]:
                        #remove string
                        #add array ['new string',[]]
                        level += 1
        
        elif command[2:4] == 'ls': #list command
            pass
    
    else: #directory or file

        if command[:3] == 'dir': #directory found
            # path += f'{command[3:]}'
            for i in dirs[level]:
                if i == command[4:]:
                    break
            dirs[level].append(command[4:])
            
        if command[0].isnumeric(): #file found
            file_ = command.split()
            dirs[level].append(file_[1])
        
#test
print(dirs)
print(level)

#process data
