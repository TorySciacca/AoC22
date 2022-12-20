"AoC Day 2 - Tory Sciacca"

total_score = 0 #Stores total game store for the player

with open('day2.txt','r') as f:
    data = f.read().split('\n') # indexes each round
    for i in data:
       round_data = i.split(' ') # indexes each move [elf_choice, player_choice]
       
       elf_choice = round_data[0]
       player_choice = round_data[1]
       
       if player_choice == 'X': #rock +1 for choice
            total_score += 1
            if elf_choice == 'B':
               total_score += 0 #Lose 
            elif elf_choice == 'A':
               total_score += 3 #Draw
            elif elf_choice == 'C':
               total_score += 6 #Win 
               
       elif player_choice == 'Y': #paper +2
            total_score += 2
            if elf_choice == 'C':
               total_score += 0 #Lose
            elif elf_choice == 'B':
                total_score += 3 #Draw
            elif elf_choice == 'A':
               total_score += 6 #Win
            
       elif player_choice == 'Z': #scissors +3
            total_score += 3
            
            if elf_choice == 'A':
             total_score += 0 #Lose
            elif elf_choice == 'C':
                total_score += 3 #Draw
            elif elf_choice == 'B':
                total_score += 6 #Win
                
print(f'The final score is {total_score}')