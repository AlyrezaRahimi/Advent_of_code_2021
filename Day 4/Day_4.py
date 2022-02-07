from json.tool import main
from os import remove


test = []
with open("F:\Work Base\Python\Advent_of_code_2021\Day 4\Test.txt") as Data:
    for i in Data:
        test.append(i.strip())
        
#get number's
main_num = test[0]
for i in range(0,len(main_num)):
    if main_num[i] == ",":
        main_num = main_num.replace(",","\n")
        
        