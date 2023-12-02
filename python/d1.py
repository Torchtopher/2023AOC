with open("d1.txt", "r") as f:
    data = f.read().split("\n")

p1 = 0
for s in data:
    digits = []
    for c in s:
        if c.isdigit():
            digits.append(c)
    p1 += int(str(digits[0]) + str(digits[-1]))

p2 = 0
nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for s in data:
    digits = []
    for idx, c  in enumerate(s):
        for num in nums:
            if s[idx:].startswith(num):
                digits.append(nums.index(num))
        if c.isdigit():
            digits.append(c)
    p2 += int(str(digits[0]) + str(digits[-1]))

print(f"Part 1 {p1}")
print(f"Part 2 {p2}")