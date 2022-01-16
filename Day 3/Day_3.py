bin_input = []

with open("F:\Work Base\Python\Advent_of_code_2021\Day 3\Test.txt") as Data3:
    for i in Data3:
        bin_input.append(i.strip())
      
epsilon = ""
gamma = ""
Bin_data = 0

num = 0  
while num < 1:
    for i in range(0,len(bin_input)):
        Bin_data = bin_input[i]
        print(Bin_data[num])
    
    
    num += 1