from ranges import Range

a = Range(1, 4)
b = Range(2, 5)

for i in range(a.intersection(b).start, a.intersection(b).end + 1):
    print(i)

with open("d5.txt", "r") as f:
    data = f.read().split("\n")

print(data)