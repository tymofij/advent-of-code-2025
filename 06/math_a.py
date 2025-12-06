from operator import add, mul

input = """
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
""".strip().split("\n")
input = open("input.txt").read().strip().split("\n")

data = [[int(y) for y in x.split()] for x in input[:-1]]
actions = [(add if x=='+' else mul) for x in input[-1].split()]

print(data)
print(actions)

res = data[0]
print("res", res)
for row in data[1:]:
    print("row", row)
    for i in range(len(row)):
        print("i", i)
        res[i] = actions[i](res[i], row[i])

print(sum(res))
