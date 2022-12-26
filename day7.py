"AoC Day 7 - Tory Sciacca"

data = open('day7.txt','r').read().split('\n') #stores each line from the data in a variable 
username = 'elf22'

directory = {}
dir_path = ''

# rfind('/') #returns index of last used of /

for command in data: #generate directory 
    
    if command[0] == '$': #function command
        
        if command[2:4] == 'cd': #change directory

            if command[5:7] == '..': #move out a level
                current_dir_size = 0
                
                for i in directory:
                    if i == dir_path:
                        current_dir_size = directory[i]
                                                
                prev_dir = dir_path.rfind('/')
                dir_path = dir_path[:prev_dir]
                
                for i in directory:
                    if i == dir_path:
                        directory.update({i:directory[i]+current_dir_size})
            
            else: 
                dir_path += str('/' + command[4:].strip())
                for i in directory:
                    if i == dir_path:
                        break
                directory.update({dir_path:0})
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
   
        if command[0].isnumeric(): #file found
            f = command.split(' ') #(f)ile
            for i in directory:
                if i == f[1]:
                    break
            directory.update({i:int(f[0])})
            # file_ = command.split()
            # dirs.append(file_[1])
    
    # if command == '$ cd cmcrzdt':
    #     break

total_under_10k = 0

for i in directory:
    if directory[i] <= 10000:
        total_under_10k += directory[i]

#test
print(directory)
print(total_under_10k) #solution: 1583951

#process data