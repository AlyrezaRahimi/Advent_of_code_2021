

points_of_lines = []


with open ("F:\Work Base\Python\Advent_of_code_2021\Day 5\line_x,y.txt", "r") as Lines:
    for point in Lines:
        points_of_lines.append(point)


#remove '->' and ','
flag = 0
first_in_the_list = 0
while flag < len(points_of_lines):
    
    point = points_of_lines[first_in_the_list]
    group_of_points = ""
    
    for counter in point:
            
        if counter == " ":
            pass
        elif counter == "-":
            pass
        elif counter == ">":
            group_of_points += ","
        else:
            group_of_points += counter
            
        
    points_of_lines.remove(points_of_lines[first_in_the_list])
    points_of_lines.append(group_of_points)
    flag += 1

#print(points_of_lines)

#remove not same x1,x2 or y1,y2


def remove_unuse_points(line):
    if int(chart_x1) != int(chart_x2) and int(chart_y1) != int(chart_y2):
        points_of_lines.remove(line)
    else:
       global lineControler
       lineControler += 1

lineControler = 0
for lines in range(0,len(points_of_lines)):
    
    line = points_of_lines[lineControler]
    chart_x1 = ""
    chart_x2 = ""
    chart_y1 = ""
    chart_y2 = ""
    counter = 0
    
    for point in line:
        
        if point == ",":
            counter += 1
        elif counter == 0:
            chart_x1 += point
        elif counter == 1:
            chart_y1 += point
        elif counter == 2:
            chart_x2 += point
        else:
            chart_y2 += point
            
    remove_unuse_points(line)   

with open("new_list.txt","w") as newList:
    for line in points_of_lines:
        newList.write(line)