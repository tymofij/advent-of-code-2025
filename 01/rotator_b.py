# count the number the dial stops at 0 -- or passes 0

nums = open("input.txt").read().split()

pos = 50
zeros = 0
for n in nums:
    dir, step = n[0], int(n[1:])
    if step > 100:
        # print("loop", n)
        zeros += (step // 100)
        step = step % 100
    if dir == "L":
        if pos != 0 and pos - step < 0:
            # print("pos", pos, "wraparound left", n)
            zeros += 1
        pos = (pos - step) % 100
    else:
        if pos != 0 and pos + step > 100:
            # print("pos", pos, "wraparound right", n)
            zeros += 1
        pos = (pos + step) % 100
    if pos == 0:
        zeros += 1

print(zeros)
