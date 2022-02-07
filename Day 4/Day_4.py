
test = []
with open("F:\Work Base\Python\Advent_of_code_2021\Day 4\Test.txt") as Data:
    for i in Data:
        test.append(i.strip())
        
#get number's
main_num = test[0]
cr_num = ""
final_num = []
i = 0

while i < len(main_num):
    if main_num[i] == ",":
        pass
    else:
        while main_num[i] != ",":
            cr_num = cr_num + main_num[i]
            i += 1
            if i == len(main_num):
                break
        final_num.append(cr_num)
        cr_num = ""
    i += 1
        
print("main number's is: ",final_num)

#get number's of matrix for loop break point
number_of_matrix = 0

for i in range(0,len(test)):
    if test[i] == "":
        number_of_matrix += 1

print("number's of matrix is: ",number_of_matrix)
