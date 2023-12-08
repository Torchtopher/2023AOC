import re

with open("d2.txt") as f:
    s = f.read().split("\n")

legal_game = {"red": 0, "green": 0, "blue": 0}
for i in s:
    # find all numbers and the word after them
    num_split = re.findall(r'\d+|[a-zA-Z]+', i)
    game_idx = num_split[1]
    
    for idx, val in enumerate(num_split):
        if val.isnumeric():
