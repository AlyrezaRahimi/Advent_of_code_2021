
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

#fix number's of matrix
def fix_matrix(cr_line):
    main_matrix_num = test[cr_line]
    matrix_num = ""
    final_matrix_num = []
    i = 0

    while i < len(main_matrix_num):
        if main_matrix_num[i] == " ":
            pass
        else:
            while main_matrix_num[i] != " ":
                matrix_num = matrix_num + main_matrix_num[i]
                i += 1
                if i == len(main_matrix_num):
                    break
            final_matrix_num.append(matrix_num)
            matrix_num = ""
        i += 1
            
    #print(final_matrix_num)
    return final_matrix_num

i = 1
start_matrix = 2
end_matrix = 7
main_matrix = {}

while i <= number_of_matrix:
    key = "matrix" + str(i)
    main_matrix.setdefault(key, [])
    
    for j in range(start_matrix,end_matrix):
       main_matrix[key].append(fix_matrix(j))
       
    start_matrix += 6
    end_matrix += 6
    i += 1   

print(main_matrix)

#comparison of matrix number with main num's

def curent_matrix(num):
    key = "matrix" + str(num)
    cr_matrix = main_matrix[key]
    return cr_matrix
    
def comparison(cr_row):
    for aray in range(0,5):
         if cr_row[aray] == curent_number:
                cr_row[aray] = "X"

def row_comparison(cr_matrix):
    row_counter = 0
   
    while row_counter < len(cr_matrix):
        cr_row = cr_matrix[row_counter]
        row_comparison = 0
        for num in range(0,5):
            if cr_row[num] == "X":
                row_comparison += 1
        if row_comparison == 5:
            return True  
        row_counter += 1
        
    
def column_comparison(cr_matrix):
    for num in range(0,5):
        column_counter = 0
        column_comparison = 0
        while column_counter < len(cr_matrix):
            cr_column = cr_matrix[column_counter]
            if cr_column[num] == "X":
                column_comparison += 1
            column_counter += 1
        if column_comparison == 5:
            return True
        
        
                
    

for i in range(0,len(final_num)):
    breakp = False
    curent_number = final_num[i]
    
    for i in range(1,number_of_matrix + 1):
        cr_matrix = curent_matrix(i)
        row_counter = 0
        
        while row_counter < len(cr_matrix):
            cr_row = cr_matrix[row_counter]
            comparison(cr_row)
            row_counter += 1
    
    #find winner matrix
    
    for num in range(1,number_of_matrix + 1):
        key = "matrix" + str(num)
        cr_matrix = main_matrix[key]
        if row_comparison(cr_matrix) or column_comparison(cr_matrix) == True:
             breakp = True
             print("the winner is: ",key," ",cr_matrix)  
             print("last number win is: ",curent_number)
             break
    
    if breakp == True:
        break
  
sum_aray = 0  
sum_matrix = main_matrix[key]
for c in range(0,len(sum_matrix)):
    cr_row = sum_matrix[c]
    for a in range(0,len(cr_row)):
        if cr_row[a] != "X":
            sum_aray = sum_aray + int(cr_row[a])
            
print("sum of other array's is: ",sum_aray)

final_score = int(curent_number) * sum_aray

print("the final score of winner is: ",final_score)