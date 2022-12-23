"AoC Day 5 - Tory Sciacca"

data = open('day5.txt','r').read() #stores each line from the data in a variable 

a,b=data.split("\n\n") #a is the crate data and b is the instructions (section a and b of data)
a,b=a.splitlines(),b.splitlines()

crates=[""]*9 #initiallizing crates into 9 empty strings within an array (9 sections)

for i in range(len(a)-2,-1,-1): #
    for j in range(1,len(a[0]), 4):
        if a[i][j].isupper():crates[j//4]+=a[i][j] #add letter to string if found
        
for i in b:
    values = i.split() #splits instructions into an array [eg: [[move] [3] [from] [2] [to] [8]]
    amount,from_crate,to_crate = int(values[1]),int(values[3])-1,int(values[5])-1 #takes values and assigns the numbers to useful variables
        
    for j in range(amount): #repeat for required amount
        crates[to_crate] += crates[from_crate][-1] #add last letter from stack a string to stack b string
        crates[from_crate] = crates[from_crate][:-1] #new string a = string a without last letter

final_output = '' #format for requrired output
for i in crates: 
    if i != []:
        final_output +=i[-1]
        
print(f'The sequence of crates at the top of each stack is: {final_output}')