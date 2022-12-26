"AoC Day 7 - Tory Sciacca"

data = open('day7.txt','r').read().split('\n') #stores each line from the data in a variable 
username = 'elf22'

directory = {'/':0}
dir_path = f'/{username}'

# rfind('/') #returns index of last used of /

for command in data: #generate directory 
    
    if command[0] == '$': #function command
        
        if command[2:4] == 'cd': #change directory

            if command[5:7] == '..': #move out a level
                dir_path = dir_path[:(dir_path.rfind('/'))]
                print(dir_path)
            
            else: 
                pass
                # for i in dirs:
                #     current_dir = command[4:].strip()
                #     if i == current_dir:
                #         print(current_dir)
                        #remove string
                        #add array ['new string',[]]
                        # level += 1

        
        elif command[2:4] == 'ls': #list command
            pass
    
    else: #directory or file

        if command[:3] == 'dir': #directory found
            dir_path += '/' + command[4:]
            for i in directory:
                if i == dir_path:
                    break
            directory.update({dir_path:0})
            
        if command[0].isnumeric(): #file found
            pass
            # file_ = command.split()
            # dirs.append(file_[1])
    
    if command == '$ cd cmcrzdt':
        break
        
#test
print(dir_path)
print(directory)

#process data