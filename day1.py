"AoC Day 1 - Tory Sciacca"

most_cal = 0 #Tracks the elf with the highest cal

with open('day1.txt','r') as f: #opens fuile
    data = f.read().split('\n\n') #breaks file down into an array containing data seperated by breaks
    for i in data:
        current_elf = i.split('\n') #breaks each elf data down
        current_cal = 0 #tracks the current elfs cals
        for i in current_elf:
            current_cal += int(i)
            
        if current_cal > most_cal: #while iterating, if the current elf has a higher number of cals than the previous record holder they overtake them
            most_cal = current_cal

print(f'The Elf carrying the most calories is carrying: {most_cal}cal')