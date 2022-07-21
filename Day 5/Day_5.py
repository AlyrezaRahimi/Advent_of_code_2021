

points_of_lines = []


with open ("F:\Work Base\Python\Advent_of_code_2021\Day 5\line_x,y.txt", "r") as Lines:
    for point in Lines:
        points_of_lines.append(point.strip())


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
    
print(points_of_lines)