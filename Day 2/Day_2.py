A = ["hello 1", "bye 2"]

c = 0

for i in range(0,2):
    b = A[i]
    if b[0] == "h":
        c = c + int(b[6])
    elif b[0] == "b":
        c = c + int(b[4])
        
print(c)