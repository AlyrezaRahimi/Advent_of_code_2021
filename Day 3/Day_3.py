bin_input = []

with open("F:\Work Base\Python\Advent_of_code_2021\Day 3\Binary input's.txt") as Data3:
    for i in Data3:
        bin_input.append(i.strip())
      
epsilon = ""
gamma = ""
Bin_data = 0
one = 0
zero = 0


num = 0  
while num < len(bin_input[0]):
    for i in range(0,len(bin_input)):
        
        Bin_data = bin_input[i]
        if int(Bin_data[num]) == 0:
            zero += 1
        elif int(Bin_data[num]) == 1:
            one += 1
            
    if zero > one:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
        
        zero = 0
        one = 0
        
    elif one > zero:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
        
        zero = 0
        one = 0
    
    num += 1
    
print("gamma is: ",gamma,"\n","epsilon is: ",epsilon)

print("Multiplication of gamma and epsilon is: ",int(gamma, 2) * int(epsilon, 2))