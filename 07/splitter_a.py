inp_lines = [line for line in open("input.txt").readlines()]
cols = len(inp_lines[0])
rows = len(inp_lines)
out_lines = [["" for _ in range(cols)] for _ in range(rows)]

n_splits = 0

stream_positions = [set() for _ in range(rows)]
for row, line in enumerate(inp_lines):
    for col, ch in enumerate(line):
        if ch == 'S':
            stream_positions[row].add(col)
        if ch == '^':
            if col in stream_positions[row-1]:
                n_splits += 1
                stream_positions[row].remove(col)
                stream_positions[row].add(max(col-1, 0))
                stream_positions[row].add(min(col+1, cols))
    if row < rows-1:
        stream_positions[row+1] = stream_positions[row]
print(n_splits)