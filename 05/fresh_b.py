# range_strs = '''
# 3-5
# 10-14
# 16-20
# 12-18
# '''.strip().split()
range_strs = open("ranges.txt").read().strip().split()
ranges = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in range_strs]
ranges.sort(key=lambda x: x[0])


def merge(a, b, c, d):
    if (a, b) == (c, d):
        return a, b
    if (c <= a <= d) or (a <= c <= b):
        return min(a, c), max(b, d)
    return a, b


separate_ranges = set()
for (a, b) in ranges:
    for (c, d) in ranges:
        a, b = merge(a, b, c, d)
    for (c, d) in ranges[::-1]:
        a, b = merge(a, b, c, d)
    separate_ranges.add((a, b))

# print(separate_ranges)

print(sum((b - a + 1) for (a,b) in separate_ranges))