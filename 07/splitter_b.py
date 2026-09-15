inp_lines = [line for line in open("input.txt").readlines()]
cols = len(inp_lines[0])
rows = len(inp_lines)
out_lines = [["" for _ in range(cols)] for _ in range(rows)]

n_splits = 0

stream_positions = [
    [0 for _ in range(cols)]
    for _ in range(rows)]
for row, line in enumerate(inp_lines):
    if row == rows-1:
        break
    for col, ch in enumerate(line):
        if ch == 'S':
            stream_positions[row+1][col] += 1
        if ch == '.':
            stream_positions[row+1][col] += stream_positions[row][col]
        if ch == '^':
            stream_positions[row+1][col-1] += stream_positions[row][col]
            stream_positions[row+1][col+1] += stream_positions[row][col]

print(sum(stream_positions[rows-1]))