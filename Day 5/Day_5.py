

points_of_lines = []


with open ("F:\Work Base\Python\Advent_of_code_2021\Day 5\line_x,y.txt", "r") as Lines:
    for point in Lines:
        points_of_lines.append(point.strip())

Lines = {}

for point in points_of_lines:
    
    start_of_line = ""
    end_of_line = ""
    group_of_points = ""
    
    for counter in point:
        
        if counter == " ":
            pass
        elif counter == "-":
            start_of_line = group_of_points
            group_of_points = ""
        elif counter == ">":
            pass
        else:
            group_of_points += counter
    end_of_line = group_of_points
    Lines[start_of_line] = end_of_line
    group_of_points = ""
    
