# range_strs = '''
# 3-5
# 10-14
# 16-20
# 12-18
# '''.strip().split()
range_strs = open("ranges.txt").read().strip().split()
ranges = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in range_strs]

# id_strs = '''
# 1
# 5
# 8
# 11
# 17
# 32
# '''.strip().split()
id_strs = open("ids.txt").read().strip().split()
ids = [int(x) for x in id_strs]

total = 0
for id in ids:
    for (a, b) in ranges:
        if a <= id <= b:
            total += 1
            break

print(total)