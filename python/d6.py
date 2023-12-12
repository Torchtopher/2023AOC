input = '''Time:        48938466
Distance:   261119210191063
'''

input = input.split("\n")
print(input)
time = input[0].split(" ")[1:]
distance = input[1].split(" ")[1:]
time = list(filter(None, time))
distance = list(filter(None, distance))
assert len(time) == len(distance)
print(time)
print(distance)

# wee native brute force, about to get slapped by pt2
total_dists = 1
for t, d in zip(time, distance):
    t, d = int(t), int(d)
    our_dists = []
    for i in range(t):
        speed = i
        our_dists.append(speed * (t - i))
    winning_dists = list(filter(lambda x: x > d, our_dists))
    #print(winning_dists)
    #print(len(winning_dists))
    total_dists *= len(winning_dists)
print(total_dists)