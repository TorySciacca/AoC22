"AoC Day 7 - Tory Sciacca"

data = open('day7.txt','r').read().split('\n') #stores each line from the data in a variable 
username = 'elftop'
directory = {}
dir_path = ''

def add_to_all_dirs(usage:int):
    f = dir_path
    
    for i in range(len(f.split('/'))-1):
        prev_dir = f.rfind('/')
        f = f[:prev_dir]
        print(dir_path,f)
        for i in directory:
            if i == f:
                directory.update({i:(directory[i]+usage)})

for command in data: #generate directory 
    
    if command[0] == '$': #function command
        
        if command[2:4] == 'cd': #change directory
            
            if command[5] == '/': #move out a level
                dir_path = username                       

            elif command[5:7] == '..': #move out a level                                           
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
                directory.update({dir_path:int(f[0])})
                add_to_all_dirs(int(f[0]))

    
total_under_10k = sum(v for v in directory.values() if v <= 100000)

print(directory)
print(total_under_10k) #solution: 1583951
