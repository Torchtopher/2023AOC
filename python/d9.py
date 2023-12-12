import re
import itertools
import numpy as np

with open('d9.txt') as f:
    data = f.read().split('\n')

print(data)
# convert each element to list of ints
data = [list(map(int, re.findall(r'-?\d+', x))) for x in data]
print(data)
ans = 0
for row in data:
    # flip row
    row = row[::-1]
    # find differences between each elemen
    # check while diffs is not all zero
    # if all zero, then we're done
    # want the reverse of diff where we extrapolate backwards
    diffs = np.diff(row)
    print(diffs)

    s = 0
    while not all(diffs == 0):
        #print(np.diff(row))
        s += diffs[-1]
        diffs = np.diff(diffs)
        print(diffs)
    ans += row[-1] + s
print(ans)





