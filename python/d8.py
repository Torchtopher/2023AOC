import itertools
import re


with open('d8.txt') as f:
    lines = f.read().split('\n')

Q = {}
cycle = itertools.cycle(lines[0])
NUM_STEPS = 10_000_000
inital_cycle = [next(cycle) for _ in range(NUM_STEPS)] 
lines = lines[2:]
print(lines)
for node in lines:
    name = node.split(" = ")[0]
    left = node.split(" = ")[1].split(", ")[0].replace("(", "")
    right = node.split(" = ")[1].split(", ")[1].replace(")", "")
    Q[name] = (left, right)
    
# all nodes is a list of all keys of Q that end with A
all_nodes = [x for x in Q.keys() if x.endswith("A")]
print(all_nodes)

steps = 0
def check_if_Z(nodes):
    # true if any node ends with Z
    #print(nodes)
    for node in nodes:
        if node.endswith("Z"):
            return True
    return False

def check_win(nodes):
    # true if all nodes end with Z
    #print(nodes)
    for node in nodes:
        if not node.endswith("Z"):
            return False
    return True

import time
# OMG TIME TO USE THE TURTLE AND THE HARE ALGORITHM
# https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare

cycle_lengths = []
# just assume like 10000 steps is enough
for starting_node in all_nodes:
    turtle_and_hare_playing_grouds = [] # literally adele
    turtle_and_hare_playing_grouds.append(starting_node)
    for dir in inital_cycle:
        dir_idx = 0 if dir == "L" else 1
        turtle_and_hare_playing_grouds.append(Q[starting_node][dir_idx])
        starting_node = Q[starting_node][dir_idx]
    #print(turtle_and_hare_playing_grouds)

    for turtle_idx, hare_idx in zip(range(NUM_STEPS+1), range(0, NUM_STEPS+2, 2)):
        if turtle_idx == hare_idx:
            continue
        #print(turtle_idx, hare_idx)
        has_Z = check_if_Z(turtle_and_hare_playing_grouds[turtle_idx: hare_idx])
        if turtle_and_hare_playing_grouds[turtle_idx].endswith("Z") and turtle_and_hare_playing_grouds[turtle_idx] == turtle_and_hare_playing_grouds[hare_idx]:
            cycle_lengths.append(hare_idx - turtle_idx)
            # print actually the cycle
            print(turtle_and_hare_playing_grouds[turtle_idx: hare_idx])
            # find indx of first occurence ending with Z

            # look up last element of cycle
            print("FOUND CYCLE with Z")
            print(turtle_and_hare_playing_grouds[turtle_idx])
            print(len(turtle_and_hare_playing_grouds[turtle_idx: hare_idx]))

            break
    
print(cycle_lengths)
#    44,810,373,917 wrong low
#   537,724,487,004 wrong
# 2,150,897,948,016 wrong
#13,129,439,557,681 CORRECT
# lcm of all cycle lengths, use numpy
import numpy as np
lcm = np.lcm.reduce(cycle_lengths)
print(lcm)
exit()


for dir in cycle:
    dir_idx = 0 if dir == "L" else 1
    for idx, node in enumerate(all_nodes):
        all_nodes[idx] = Q[node][dir_idx]
    steps += 1
    if check_win(all_nodes):
        break

print(steps)