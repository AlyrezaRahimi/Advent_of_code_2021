
input_data = []

with open("X") as Data_2:
    for i in Data_2:
        input_data.append(i.strip())
#X is path of input's data
        
H = 0
W = 0

#forward X
#up X
#down X  
        
for i in range(0,len(input_data)):
    word = input_data[i]
    if word[0] == "f":
        H = H + int(word[8])
    elif word[0] == "u":
        W = W - int(word[3])
    elif word[0] == "d":
        W = W + int(word[5])
        
print("position X:",H,"--->","position Y:",W,"--->","X*Y:",H*W)
