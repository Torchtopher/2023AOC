import itertools
# import a deueque
from collections import deque

with open('d10.txt', 'r') as f:
    data = f.read().split('\n')

print(data)
# find starting position
start_row_idx = 0
start_col_idx = 0

for line in data:
    if "S" in line:
        start_row_idx = data.index(line)
        start_col_idx = line.index("S")
        break
print(start_row_idx, start_col_idx)
path_1_row_idx = 0
path_1_col_idx = 0

path_2_row_idx = 0
path_2_col_idx = 0

SOUTH_CHARS = ["|", "7", "F"]
NORTH_CHARS = ["|", "J", "L"]
EAST_CHARS = ["-", "L", "F"]
WEST_CHARS = ["-", "J", "7"]
# check the 4 directions around the starting position and see if there are valid paths
# if there are, then we can start the path there
for row_idx in range(start_row_idx - 1, start_row_idx + 2):
    for col_idx in range(start_col_idx - 1, start_col_idx + 2):
        if row_idx == start_row_idx and col_idx == start_col_idx:
            continue
        if row_idx < 0 or row_idx > len(data) - 1:
            continue
        if col_idx < 0 or col_idx > len(data[0]) - 1:
            continue
        if data[row_idx][col_idx] == ".":
            continue
        # we are above the starting position so we need south chars
        if row_idx == start_row_idx - 1 and col_idx == start_col_idx:
            if data[row_idx][col_idx] in SOUTH_CHARS:
                if path_1_col_idx == 0 and path_1_row_idx == 0:
                    path_1_row_idx = row_idx
                    path_1_col_idx = col_idx
                else:
                    path_2_row_idx = row_idx
                    path_2_col_idx = col_idx
                print("found path")
                print(row_idx, col_idx)
                print(data[row_idx][col_idx])

        # we are below the starting position so we need north chars
        if row_idx == start_row_idx + 1 and col_idx == start_col_idx:
            if data[row_idx][col_idx] in NORTH_CHARS:
                if path_1_col_idx == 0 and path_1_row_idx == 0:
                    path_1_row_idx = row_idx
                    path_1_col_idx = col_idx
                else:
                    path_2_row_idx = row_idx
                    path_2_col_idx = col_idx
                print("found path")
                print(row_idx, col_idx)
                print(data[row_idx][col_idx])
        
        # we are to the left of the starting position so we need east chars
        if row_idx == start_row_idx and col_idx == start_col_idx - 1:
            if data[row_idx][col_idx] in EAST_CHARS:
                if path_1_col_idx == 0 and path_1_row_idx == 0:
                    path_1_row_idx = row_idx
                    path_1_col_idx = col_idx
                else:
                    path_2_row_idx = row_idx
                    path_2_col_idx = col_idx
                print("found path 3")
                print(row_idx, col_idx)
                print(data[row_idx][col_idx])

        # we are to the right of the starting position so we need west chars
        if row_idx == start_row_idx and col_idx == start_col_idx + 1:
            if data[row_idx][col_idx] in WEST_CHARS:
                if path_1_col_idx == 0 and path_1_row_idx == 0:
                    path_1_row_idx = row_idx
                    path_1_col_idx = col_idx
                else:
                    path_2_row_idx = row_idx
                    path_2_col_idx = col_idx
                print("found path 4")
                print(row_idx, col_idx)
                print(data[row_idx][col_idx])

VISITED_SET = set()
VISITED_SET.add((path_1_row_idx, path_1_col_idx))
VISITED_SET.add((path_2_row_idx, path_2_col_idx))
VISITED_SET.add((start_row_idx, start_col_idx))
visited_list_p1 = []
visited_list_p2 = [] 

print(path_1_row_idx, path_1_col_idx)
print(path_2_row_idx, path_2_col_idx)
steps = 1

def move_path(row_idx=None, col_idx=None):
    #print(row_idx, col_idx)
    dir = data[row_idx][col_idx]
    
    if dir == "|":
        if (row_idx + 1, col_idx) not in VISITED_SET:
            return row_idx + 1, col_idx
        if (row_idx - 1, col_idx) not in VISITED_SET:
            return row_idx - 1, col_idx
        assert False
    
    if dir == "-":
        if (row_idx, col_idx + 1) not in VISITED_SET:
            return row_idx, col_idx + 1
        if (row_idx, col_idx - 1) not in VISITED_SET:
            return row_idx, col_idx - 1
        assert False
    
    if dir == "L":
        if (row_idx - 1, col_idx) not in VISITED_SET:
            return row_idx - 1, col_idx
        if (row_idx, col_idx + 1) not in VISITED_SET:
            return row_idx, col_idx + 1
        assert False
    
    if dir == "J":
        if (row_idx - 1, col_idx) not in VISITED_SET:
            return row_idx - 1, col_idx
        if (row_idx, col_idx - 1) not in VISITED_SET:
            return row_idx, col_idx - 1
        assert False
    
    if dir == "7":
        if (row_idx + 1, col_idx) not in VISITED_SET:
            return row_idx + 1, col_idx
        if (row_idx, col_idx - 1) not in VISITED_SET:
            return row_idx, col_idx - 1
        assert False

    if dir == "F":
        if (row_idx + 1, col_idx) not in VISITED_SET:
            return row_idx + 1, col_idx
        if (row_idx, col_idx + 1) not in VISITED_SET:
            return row_idx, col_idx + 1
        assert False
    assert False

def visualize_visited(possible):
    # put a V where we have visited
    for row_idx, row in enumerate(data):
        for col_idx, col in enumerate(row):
            
            if (row_idx, col_idx) in VISITED_SET:
                print("V", end="")
            elif (row_idx, col_idx) in possible:
                print("P", end="")
            else:
                print(col, end="")
        print()

def visualize_data(current_point_p1=None, current_point_p2=None):
    if current_point_p1:
        for row_idx, row in enumerate(data):
            for col_idx, col in enumerate(row):
                if row_idx == current_point_p1[0] and col_idx == current_point_p1[1]:
                    print("X", end="")
                elif row_idx == current_point_p2[0] and col_idx == current_point_p2[1]:
                    print("O", end="")
                else:
                    print(col, end="")
                
            print()
        return
    else:
        for row in data:
            print(row)
visited_list_p1.append((start_row_idx, start_col_idx))
# add it to the start of p2 instead of the end
visited_list_p2.insert(0, (start_row_idx, start_col_idx))
visited_list_p1.append((path_1_row_idx, path_1_col_idx))
visited_list_p2.append((path_2_row_idx, path_2_col_idx))
#visualize_data(current_point_p1=(path_2_row_idx, path_2_col_idx), current_point_p2=(path_1_row_idx, path_1_col_idx))
while path_1_col_idx != path_2_col_idx or path_1_row_idx != path_2_row_idx:
    steps += 1
    VISITED_SET.add((path_1_row_idx, path_1_col_idx))
    VISITED_SET.add((path_2_row_idx, path_2_col_idx))

    path_1_row_idx, path_1_col_idx = move_path(row_idx=path_1_row_idx, col_idx=path_1_col_idx)
    path_2_row_idx, path_2_col_idx = move_path(row_idx=path_2_row_idx, col_idx=path_2_col_idx)
    visited_list_p1.append((path_1_row_idx, path_1_col_idx))
    visited_list_p2.append((path_2_row_idx, path_2_col_idx))
    #visualize_data(current_point_p1=(path_2_row_idx, path_2_col_idx), current_point_p2=(path_1_row_idx, path_1_col_idx))

print(steps)
dots = []

# get index of all dots
for row_idx, row in enumerate(data):
    for col_idx, col in enumerate(row):
        if (row_idx, col_idx) not in VISITED_SET:
            dots.append((row_idx, col_idx))


print(VISITED_SET)
from shapely.geometry import Point, Polygon
import matplotlib.path
import matplotlib.pyplot as plt
# Create a square
visualize_visited(dots)
# reverse p2 list
visited_list_p2.reverse()
visited_list_p2.pop(0)
# combine the two lists
visited_list_p1.extend(visited_list_p2)
path = matplotlib.path.Path(visited_list_p1)
plt.plot(*path.vertices.T, 'o-')
plt.show() 
part2 = 0 
poly = Polygon(visited_list_p1)
for dot in dots:
    point = Point(dot)
    if poly.contains(point):
        part2 += 1
        print(dot)
print(part2)