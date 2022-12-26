"AoC Day 7 - Tory Sciacca"

data = open('day7.txt','r').read().split('\n') #stores each line from the data in a variable 
username = 'elf22'

directory = {}
dir_path = ''

for command in data: #generate directory 
    
    if command[0] == '$': #function command
        
        if command[2:4] == 'cd': #change directory

            if command[5:7] == '..': #move out a level
                current_dir_size = 0                                              
                prev_dir = dir_path.rfind('/')
                dir_path = dir_path[:prev_dir]
                           
            else: 
                dir_path += str('/' + command[4:].strip())
                if dir_path not in directory:
                    directory.update({dir_path:0})

        elif command[2:4] == 'ls': #list command
            continue
    
    else: #directory or file
   
        if command[0].isnumeric(): #file found
            found = False
            f = command.split(' ') #(f)ile
            for i in directory:
                if i == f[1]:
                    found = True
                    
            if not found:
                directory.update({i:int(f[0])})

def add_to_all_dirs(dir_path):
    # dir_path
    pass

total_under_10k = sum(v for v in directory.values() if v <= 100000)

print(directory)
print(total_under_10k) #solution: 1583951