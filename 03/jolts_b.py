input = """
987654321111111
811111111111119
234234234234278
818181911112111
""".strip()

input = open("input.txt").read()

sum = 0
for line in input.split():
    nums = []
    print(line)
    start = 0
    for i in range(11, -1, -1):
        if i != 0:
            searched = line[start: -i]
        else:
            searched = line[start:]
        print("searched=", searched, "i=", i, "start", start)
        m = max(searched)
        print("m=", m)
        pos = searched.find(m)
        print("pos=", pos)
        nums.append(m)
        start += pos + 1
        print("new_start", start)
        print()

    nums = "".join(nums)
    print("res", nums)
    sum += int(nums)
print()
print("sum", sum)