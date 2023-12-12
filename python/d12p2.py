import itertools
import functools
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

@functools.lru_cache(maxsize=None)
def recursive_is_valid(LINE, BLOCKS, current_block_len, debug_string=""):
    #print(LINE, BLOCKS, current_block_len, debug_string)
    if LINE == "":
        if BLOCKS == ():
            #print("VALID")
            
            #print(debug_string)
            #print("====")
            return 1
        else:
            #print("INVALID", current_block_len, BLOCKS)
            return 0
    if BLOCKS == ():
        if current_block_len == 0 and not "#" in LINE:
            return 1
        else:
            return 0
        
    next_char = "Z"
    if len(LINE) > 1:
        next_char = LINE[1]
    if LINE.startswith("."):
        #print("\nADDING .")
        if current_block_len == 0:
            return recursive_is_valid(LINE[1:], BLOCKS, 0, "." + LINE[1:])
        else:
            return 0 
        #return recursive_is_valid(LINE[1:], BLOCKS, 0, "." + LINE[1:])
    if LINE.startswith("#"):
        #print("\nADDING #")
        current_block_len += 1
        if current_block_len == BLOCKS[0] and (next_char != "#"):
            return recursive_is_valid(LINE[2:], BLOCKS[1:], 0, "#." + LINE[2:])
        else:
            return recursive_is_valid(LINE[1:], BLOCKS, current_block_len, "#" + LINE[1:]) # continue the block
    if LINE.startswith("?"):
        ans = 0
        # dot case
        if current_block_len == 0:
            #print("\nADDING .")
            ans += recursive_is_valid(LINE[1:], BLOCKS, 0, "." + LINE[1:])

        # hash case
        current_block_len += 1
        if current_block_len == BLOCKS[0] and next_char != "#": 
            #print("FINISHING BLOCK")
            ans += recursive_is_valid(LINE[2:], BLOCKS[1:], 0, "#." + LINE[2:])
        else:
            ans += recursive_is_valid(LINE[1:], BLOCKS, current_block_len, "#" + LINE[1:]) # continue the block
        return ans

#print(recursive_is_valid(".??..??...?##.", [1,1,3], 0))    
#exit()
assert recursive_is_valid("???.###", (1,1,3), 0) == 1
assert recursive_is_valid(".??..??...?##.", (1,1,3), 0) == 4
#print(recursive_is_valid("?#?#?#?#?#?#?#?", [1,3,1,6], 0))
assert recursive_is_valid("?#?#?#?#?#?#?#?", (1,3,1,6), 0) == 1
assert recursive_is_valid("????.#...#...", (4,1,1), 0) == 1
#print(recursive_is_valid("????.######..#####.", (1,6,5), 0))
assert recursive_is_valid("????.######..#####.", (1,6,5), 0, "") == 4#, (recursive_is_valid("????.######..#####.", (1,6,5), 0, ""), recursive_is_valid.cache_info())
#print(recursive_is_valid("????.######..#####.", (1,6,5), 0, ""))
assert recursive_is_valid("?###????????", (3,2,1), 0) == 10
print("HOLY SHIT TESTS PASSED")

ans = 0
for l in data:
    line = l.split(" ")[0] + "?" + l.split(" ")[0] + "?" + l.split(" ")[0] + "?" + l.split(" ")[0] + "?" + l.split(" ")[0]
    #line = l.split(" ")[0]
    print(line)
    broken = (l.split(" ")[1] + ",") * 5
    broken = broken[:-1]
    #broken = l.split(" ")[1]
    print(broken)
    broken = broken.split(",")
    broken = [int(x) for x in broken]
    # convert broken to a tuple
    broken = tuple(broken)
    q_len = line.count("?")
    print(broken)
    ans += recursive_is_valid(line, broken, 0)
print(ans)    