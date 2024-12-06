# Parse input

with open("Day 4/input.txt", "r") as f:
    inp = f.readlines()

inp = [line.strip() for line in inp]

# Part 1

def count_xmas(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    def is_valid(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_valid(x, y, dx, dy):
                    count += 1
    return count

result = count_xmas(inp)
#print(result)

# Part 2

def count_xmas_diagonal(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            if r + 2 < rows and c + 2 < cols and grid[r][c] == 'M' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'S' and grid[r + 2][c] == 'M' and grid[r][c + 2] == 'S':
                count += 1
            if r + 2 < rows and c + 2 < cols and grid[r][c] == 'M' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'S' and grid[r + 2][c] == 'S' and grid[r][c + 2] == 'M':
                count += 1
            if r + 2 < rows and c + 2 < cols and grid[r][c] == 'S' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'M' and grid[r + 2][c] == 'M' and grid[r][c + 2] == 'S':
                count += 1
            if r + 2 < rows and c + 2 < cols and grid[r][c] == 'S' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'M' and grid[r + 2][c] == 'S' and grid[r][c + 2] == 'M':
                count += 1
    return count

grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]


print(count_xmas_diagonal(inp))