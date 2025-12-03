input = """
987654321111111
811111111111119
234234234234278
818181911112111
""".strip()
input = open("input.txt").read().split()

sum = 0
for line in input:
    m1 = max(line[:-1])
    pos1 = line.find(m1)
    # print(m1, pos1)
    m2 = max(line[pos1+1:])
    # print(line[pos1+1:], m2)
    # print(m1+m2)
    sum += int(m1+m2)
print(sum)