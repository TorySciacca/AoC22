"AoC Day 7 - Tory Sciacca"

data = open('day7.txt','r').read().split('\n') #stores each line from the data in a variable 
username = 'elftop'
directory = {}
dir_path = ''

def add_to_all_dirs(usage:int): #the brief requrires parent directories to include the child usage in the summof every directory
    f = dir_path
    
    for i in range(len(f.split('/'))):
        for i in directory:
            if i == f:
               directory[i] += usage
        prev_dir = f.rfind('/')
        f = f[:prev_dir]

for command in data: #generate directory 
    
    if command[0] == '$': #function command
        
        if command[2:4] == 'cd': #change directory
            
            if command[5] == '/': #intital folder (useful to have a name)
                dir_path = username                       

            elif command[5:7] == '..': #move out a level                                           
                prev_dir = dir_path.rfind('/')
                dir_path = dir_path[:prev_dir]
                           
            else: # update directory path
                dir_path += str('/' + command[4:].strip())
                
            if dir_path not in directory: #if path is new
                directory.update({dir_path:0})

    else: #file
   
        if command[0].isnumeric(): #file found
            f = command.split(' ') #(f)ile splits into usage,filename 
            add_to_all_dirs(int(f[0])) #updates every dir in path to include file usage 
                
result = sum(v for v in directory.values() if v <= 100000)

# print(directory)
print(f'The sum total of every directory (under 100,000) is: {result}') 