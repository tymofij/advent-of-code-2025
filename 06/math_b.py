from operator import add, mul
from functools import reduce

input = """
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
""".strip().split("\n")
input = open("input.txt").read().strip().split("\n")

n_rows = len(input)-1
max_len = max(len(line) for line in input)
input = [line.ljust(max_len) for line in input]
signs = input[-1].ljust(max_len)
i = 0
start = 0
numbers = []
actions = []
while i <= max_len:
    if i == max_len:
        num = []
        for j in range(n_rows):
            num.append(input[j][start:])
        numbers.append(num)
        break

    if signs[i] in ('+', '*'):
        num = []
        for j in range(n_rows):
            num.append(input[j][start:i-1])
        if i != 0:
            numbers.append(num)

        action = add if signs[i] == '+' else mul
        actions.append(action)

        start = i
        i += 1
        continue

    if signs[i] == ' ':
        i += 1
        continue

def cephalopod_nums(s):
    nums = []
    for col in range(len(s[0])):
        res = ''
        for row in range(len(s)):
            res += s[row][col]
        nums.append(res)
    return [int(x) for x in nums]

# print(cephalopod_nums(['123', ' 45', '  6']))

total = 0
for i in range(len(numbers)):
    # print(actions[i])
    # print(cephalopod_nums(numbers[i]))
    # print()
    total += reduce(actions[i], cephalopod_nums(numbers[i]))

print(total)

# print(numbers)
# print(actions)