from collections import defaultdict

class DefaultDict(defaultdict):
    def __missing__(self, key):
        return self.default_factory(key)
d = DefaultDict(lambda key: key)


with open("d5.txt", "r") as f:
    data = f.read().strip().split("\n\n")

data = list(filter(None, data)) 
print(data)
ans = 0

seeds = data[0].split(": ")[1].split(" ")
seeds = [int(x) for x in seeds]
# itterate over pairs of values in seeds
new_seeds = []
for i in range(0, len(seeds), 2):
    new_seeds.append(range(seeds[i], seeds[i] + seeds[i + 1]))
seeds = new_seeds
print(seeds)
print(new_seeds)
print(seeds)
data.pop(0)
list_of_maps = []

for map_input in data:
    map_input = map_input.split("\n")
    #print(map_input)
    #print("="*100)
    map_str = map_input[0].split(" map:")[0]
    map_input.pop(0)
    #print(map_input)
    # convert from list of strings to list of list of ints
    # is this haskell
    map_input = [list(map(int, x.split(" "))) for x in map_input]
    #print(map_input)
    Q = {} # source range -> target range
    for r in map_input:
        Q[range(r[1], r[1] + r[2])] = range(r[0], r[0] + r[2])
    #print(Q)
    #print("*"*100)
    list_of_maps.append(Q)

m = 100000000000000000
for s in seeds:
    for seed in s:
        for idx, map_ in enumerate(list_of_maps):
            for key, val in map_.items():
                if seed in key:
                    seed = val[seed - key.start]
                    break
        if seed < m:
            m = seed
    #print(seed)
print(m)
    
    