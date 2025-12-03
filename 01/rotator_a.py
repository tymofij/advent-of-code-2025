# count the number the dial stops at 0

nums = open("input.txt").read().split()

pos = 50
zeros = 0
for n in nums:
    dir, step = n[0], int(n[1:])
    if dir == "L":
        pos = (pos - step) % 100
    else:
        pos = (pos + step) % 100
    if pos == 0:
        zeros += 1

print(zeros)
