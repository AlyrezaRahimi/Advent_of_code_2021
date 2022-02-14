<<<<<<< HEAD
=======

>>>>>>> ad673babc45225105887c85d5cd1e302ed03560c
bin_input = []

with open("X") as Data3:
    for i in Data3:
        bin_input.append(i.strip())
#X is path of input's data
        
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
<<<<<<< HEAD

print("Multiplication of gamma and epsilon is: ",int(gamma, 2) * int(epsilon, 2))
=======
print("Multiplication of gamma and epsilon is: ",int(gamma, 2) * int(epsilon, 2))
>>>>>>> ad673babc45225105887c85d5cd1e302ed03560c
