inp_lines = [line for line in open("input.txt").readlines()]
cols = len(inp_lines[0])
rows = len(inp_lines)

start_pos = inp_lines[0].index('S')
prev_paths = set()
prev_paths.add((start_pos,))

for row in range(1, rows):
    print(row)
    new_paths = set()
    for prev_path in prev_paths:
        # print(f"evaluating {prev_path}, row {row}")
        col = prev_path[-1]
        ch = inp_lines[row][col]
        if ch == '.':
            # print(f"passing down, pos {col}, row {row}")
            new_paths.add(prev_path + (col,))
        if ch == '^':
            new_paths.add(prev_path + (col-1,))
            new_paths.add(prev_path + (col+1,))

    prev_paths = new_paths

print(len(prev_paths))