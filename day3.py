"AoC Day 3 - Tory Sciacca"

priority_sum = 0 #stores total sum of priotity items

priority_index = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(priority_index)):
    priority_index.append(priority_index[i].upper()) 

with open('day3.txt','r') as f:
    data = f.read().split('\n') # seperates each sack
    for i in data: 
        priority_item = '' 
        compartment_a = []
        compartment_b = []
        compartment_size = round(len(i)/2) #each compartment should be split into two even sides
        
        for j in range(compartment_size): #indexes each size into seperate arrays
            compartment_a.append(i[j]) 
            compartment_b.append(i[j+compartment_size])
            
        for j in compartment_a: #compares every item in comp_a with every item in comp_b
            for k in compartment_b:
                if j == k:
                    priority_item = j
                    break #no need to keep searching if found
                    
        priority_sum += priority_index.index(priority_item) + 1 #retrives index of found priority item, +1 since 'a' should be worth 1, 'b': 2 and so on
        
print(f'The total sum of priority items is: {priority_sum}')