
input_data = []

with open("F:\Work Base\Python\Advent_of_code_2021\Day 1\Data.txt") as Data:
    for i in Data:
        input_data.append(i)
        
counter_change = 0
input_data_num = int(input_data[0])

for i in range(1,len(input_data)):
    if int(input_data[i]) > input_data_num:
        input_data_num = int(input_data[i])
        counter_change += 1
        print(input_data[i])
    else:
        input_data_num = int(input_data[i])

print("number of change's",counter_change)