import itertools
with open("d12.txt", "r") as f:
    data = f.read().split("\n")

print(data)

cache = {}

def is_valid(line, block, replacments):
    # replace corresponding ? with replacments
    for char in line:
        if char == "?":
            line = line.replace("?", replacments.pop(0), 1)

    #print(line)
    #print(block)
    '''#.#.###
       [1, 1, 3]
    '''
    # get lenghts of continous #'s
    lengths = []
    current = 0
    for char in line:
        #print(char)
        if char == "#":
            current += 1
        else:
            if current > 0:
                lengths.append(current)
            current = 0
    if current > 0:
        lengths.append(current)
    if lengths == block:
        return True
    return False

assert is_valid("???.###", [1,1,3], ["#", ".", "#"]) == True
assert is_valid("???.###", [1,1,3], ["#", "#", "#"]) == False

ans = 0
for l in data:
    line = l.split(" ")[0]
    broken = l.split(" ")[1]
    broken = broken.split(",")
    broken = [int(x) for x in broken]
    q_len = line.count("?")
    print(broken)
    
    for p in itertools.product("#.", repeat=q_len):
        print(list(p))
        #print("----------------")
        if is_valid(line, broken, list(p)):
            ans += 1
            print("valid")
print(ans)    