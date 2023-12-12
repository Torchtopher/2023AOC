from copy import deepcopy
import itertools

with open("d11.txt") as f:
    data = f.read().split("\n")

print(data)
# hoizontal lines
to_loop = list(enumerate(data))
lines_added = 0
for idx, line in to_loop:
    # check if line just has .
    if line == "." * len(line):
        print("Line is just dots 1")
        # insert line with all dots right before this line
        data.insert(idx + lines_added, "9" * len(line))
        lines_added += 1 

data = list(map(list, zip(*data)))
data = list(map(lambda x: "".join(x), data))

to_loop = list(enumerate(data))
lines_added = 0
for idx, line in to_loop:
    # check if line just has . or 9
    
    if all([x == "." or x == "9" for x in line]):
        print("Line is just dots")
        # insert line with all dots right before this line
        data.insert(idx + lines_added, "9" * len(line))
        lines_added += 1 

data = list(map(list, zip(*data)))

data = list(map(lambda x: "".join(x), data))

# get indexes of all # characters
occupied = []
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == "#":
            occupied.append((row, col))

#print(occupied)
# pairs with itertools
pairs = list(itertools.combinations(occupied, 2))
# find taxicab distance between pairs
ans = 0
TO_ADD = 999999
for pair in pairs:
    print(pair)
    p1 = pair[0]
    p2 = pair[1]
    if p1[0] < p2[0]:
        # p1 is above p2
        # check if there is a dot between them
        for i in range(p1[0], p2[0]):
            if data[i][p1[1]] == "9":
                ans += TO_ADD
            else:
                ans += 1
    elif p1[0] > p2[0]:
        # p1 is below p2
        for i in range(p2[0], p1[0]):
            if data[i][p1[1]] == "9":
                ans += TO_ADD
            else:
                ans += 1

    if p1[1] < p2[1]:
        # p1 is left of p2
        for i in range(p1[1], p2[1]):
            if data[p1[0]][i] == "9":
                ans += TO_ADD
            else:
                ans += 1

    elif p1[1] > p2[1]:
        # p1 is right of p2
        for i in range(p2[1], p1[1]):
            if data[p1[0]][i] == "9":
                ans += TO_ADD
            else:
                ans += 1        
    
for row in data:
    print(row)
print(ans)