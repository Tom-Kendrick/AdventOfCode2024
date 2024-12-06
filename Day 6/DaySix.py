# Parse Input

with open("Day 6/input.txt", "r") as f:
    inp = f.readlines()
grid = [line.strip() for line in inp]

# Part 1

def move_guard(grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_index = 0 
    
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char in '^>v<':
                start_pos = (r, c)
                dir_index = '^>v<'.index(char)
                break

    visited_positions = set() 
    row, col = start_pos
    visited_positions.add((row, col))

    def replace_char_in_grid(grid, row, col, new_char):
        grid[row] = grid[row][:col] + new_char + grid[row][col+1:]

    while True:
        next_row = row + directions[dir_index][0]
        next_col = col + directions[dir_index][1]

        if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
            break

        if grid[next_row][next_col] == '#':
            dir_index = (dir_index + 1) % 4
        else:
            replace_char_in_grid(grid, row, col, '.') 
            row, col = next_row, next_col
            replace_char_in_grid(grid, row, col, '^>v<'[dir_index])
            visited_positions.add((row, col))
    
    return len(visited_positions)


distinct_positions = move_guard(grid)

print(f"Distinct positions visited: {distinct_positions}")
