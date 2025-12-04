import copy

data = '''
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
'''.strip().split()

data = open("input.txt").read().split()

input = [list(row) for row in data]

shifts = ((-1, -1), (-1, 0), (-1, 1),
          (0,  -1),          (0,  1),
          (1,  -1), (1,  0), (1,  1))

max_row = len(input)-1
max_col = len(input[0])-1
total = 0

new = copy.deepcopy(input)
has_change = True

while has_change:
    has_change = False
    new = copy.deepcopy(input)
    for row in range(max_row+1):
        for col in range(max_col+1):
            new[row][col] = input[row][col]
            n = 0
            if input[row][col] != '@':
                continue
            for (a, b) in shifts:
                r, c = row + a, col + b
                if (r>=0 and c>=0 and r<=max_row and c<=max_col
                    and input[r][c] == "@"):
                    n += 1
            if n < 4:
                total += 1
                new[row][col] = '.'
                has_change = True
    input = copy.deepcopy(new)

print(total)
