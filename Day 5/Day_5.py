
points_of_lines = []


with open ("F:\Work Base\Python\Advent_of_code_2021\Day 5\line_test.txt", "r") as Lines:
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
        
#Checking the intersection of points
def Calculation_of_intersection_inside_points_vertical():
    global number_of_intersection
    number_of_intersection = 0
    inside_vertical_difference_line1 = abs(int(line_y2) - int(line_y1)) 
    inside_vertical_difference_line2 = abs(int(Ch_line_y2) - int(Ch_line_y1))
    if inside_vertical_difference_line1 > inside_vertical_difference_line2: 
        for sum in range(int(Ch_line_y1),int(Ch_line_y2) + 1):
            number_of_intersection += 1
        return number_of_intersection
    else:
        for sum in range(int(line_y1),int(line_y2) + 1):
            number_of_intersection += 1
        return number_of_intersection

def Calculation_of_intersection_outside_points_vertical():
    global number_of_intersection
    number_of_intersection = 0
    if int(Ch_line_y1) < int(line_y1):
        outside_vertical_difference_line1 = int(Ch_line_y2) - int(line_y1)
        number_of_intersection = outside_vertical_difference_line1
        return number_of_intersection
    elif int(Ch_line_y2) > int(line_y2):
        outside_vertical_difference_line2 = int(line_y2) - int(Ch_line_y1)
        number_of_intersection = outside_vertical_difference_line2
        return number_of_intersection
    elif int(Ch_line_y1) == int(line_y2) or int(Ch_line_y2) == int(line_y1):
        number_of_intersection += 1
        return number_of_intersection

def Calculation_of_intersection_inside_points_horizental():
    global number_of_intersection
    number_of_intersection = 0
    inside_horizental_difference_line1 = int(line_x2) - int(line_x1)
    inside_horizental_difference_line2 = int(Ch_line_x2) - int(Ch_line_x1)
    if inside_horizental_difference_line1 > inside_horizental_difference_line2:
        for sum in range(int(Ch_line_x1),int(Ch_line_x2) + 1):
            number_of_intersection += 1
        return number_of_intersection
    else:
        for sum in range(int(line_x1),int(line_x2) + 1):
            number_of_intersection += 1
        return number_of_intersection

def Calculation_of_intersection_outside_points_horizental():
    global number_of_intersection
    number_of_intersection = 0
    if int(Ch_line_x1) < int(line_x1):
        outside_horizental_difference_line1 = int(Ch_line_x2) - int(line_x1)
        number_of_intersection = outside_horizental_difference_line1
        return number_of_intersection
    elif int(Ch_line_x2) > int(line_x2):
        outside_horizental_difference_line2 = int(line_x2) - int(Ch_line_x1)
        number_of_intersection = outside_horizental_difference_line2
        return number_of_intersection
    elif int(Ch_line_x1) == int(line_x2) or int(Ch_line_x2) == int(line_x1):
        number_of_intersection += 1
        return number_of_intersection

def Calculation_of_intersection_one_point_vertical():
    global number_of_intersection
    number_of_intersection = 0
    for mainLinePoint in range(int(line_y1),int(line_y2)):
        for pointX in range(int(Ch_line_x1),int(Ch_line_x2)):
            for pointY in range(int(Ch_line_y1),int(Ch_line_y2)):
                if int(line_x1) == pointX and mainLinePoint == pointY:
                    number_of_intersection += 1
                    return number_of_intersection

def Calculation_of_intersection_one_point_horizental():
    global number_of_intersection
    number_of_intersection = 0
    for mainLinePoint in range(int(line_x1),int(line_x2)):
        for pointX in range(int(Ch_line_x1),int(Ch_line_x2)):
            for pointY in range(int(Ch_line_y1),int(Ch_line_y2)):
                if mainLinePoint == pointX and int(line_y1) == pointY:
                    number_of_intersection += 1
                    return number_of_intersection
                
number_of_intersection_points = 0
markerOflines = 1

for line in points_of_lines:

    counter = 0
    line_x1 = ""
    line_x2 = ""
    line_y1 = ""
    line_y2 = ""
    
    for point in line:
        
        if point == ",":
            counter += 1
        elif counter == 0:
            line_x1 += point
        elif counter == 1:
            line_y1 += point
        elif counter == 2:
            line_x2 += point
        elif point =="\n":
            pass
        else:
            line_y2 += point 
    
    for CheckLine in range(markerOflines,len(points_of_lines)):
        Comparison_line = points_of_lines[CheckLine]
        counter = 0
        Ch_line_x1 = ""
        Ch_line_x2 = ""
        Ch_line_y1 = ""
        Ch_line_y2 = ""
        
        for point in Comparison_line:
            
            if point == ",":
                counter += 1
            elif counter == 0:
                Ch_line_x1 += point
            elif counter == 1:
                Ch_line_y1 += point
            elif counter == 2:
                Ch_line_x2 += point
            elif point =="\n":
                pass
            else:
                Ch_line_y2 += point
        
        if line_x1 == line_x2 and Ch_line_x1 == Ch_line_x2 or line_y1 == line_y2 and Ch_line_y1 == Ch_line_y2:
            if line_x1 == Ch_line_x1 and line_x2 == Ch_line_x2:
                if int(line_y1) == int(Ch_line_y1) or int(line_y2) == int(Ch_line_y2) or int(line_y2) > int(Ch_line_y2) and int(line_y2) > int(Ch_line_y2) or int(Ch_line_y1) > int(line_y1):
                    Calculation_of_intersection_inside_points_vertical()
                    number_of_intersection_points += number_of_intersection 
                else:
                    Calculation_of_intersection_outside_points_vertical()
                    number_of_intersection_points += number_of_intersection 
            elif line_y1 == Ch_line_y1 and line_y2 == Ch_line_y2:
                if int(line_x1) == int(Ch_line_x1) or int(line_x2) == int(Ch_line_x2) or int(line_x2) > int(Ch_line_x2) and int(line_x2) > int(Ch_line_x2) or int(Ch_line_x1) > int(line_x1):
                    Calculation_of_intersection_inside_points_horizental()
                    number_of_intersection_points += number_of_intersection 
                else:
                    Calculation_of_intersection_outside_points_horizental()
                    number_of_intersection_points += number_of_intersection 
            else:
                pass
        elif line_x1 == line_x2 and Ch_line_x1 != Ch_line_x2 or line_y1 == line_y2 and Ch_line_y1 != Ch_line_y2:
            if line_x1 == line_x2:
                Calculation_of_intersection_one_point_vertical()
                number_of_intersection_points += number_of_intersection
            elif line_y1 == line_y1:
                Calculation_of_intersection_one_point_horizental()
                number_of_intersection_points += number_of_intersection
    markerOflines += 1
    
    
print(number_of_intersection_points)

        

