import copy

def accessible_paper_rolls(grid):
  n = len(grid[0])
  m = len(grid)
  total = 1
  grand_total = 0
  while total != 0:
    total = 0
    new_grid = copy.deepcopy(grid)
    for i in range(n):
      for j in range(m):
        neighbours = 0
        if grid[i][j] != "@": continue
        if i < n-1 and grid[i+1][j] == "@": neighbours += 1
        if i > 0 and grid[i-1][j] == "@": neighbours += 1
        if j < m-1 and grid[i][j+1] == "@": neighbours += 1
        if j > 0 and grid[i][j-1] == "@": neighbours += 1
        if i > 0 and j > 0 and grid[i-1][j-1] == "@": neighbours += 1
        if i < n-1 and j < m-1 and grid[i+1][j+1] == "@": neighbours += 1
        if i > 0 and j < m-1 and grid[i-1][j+1] == "@": neighbours += 1
        if i < n-1 and j > 0 and grid[i+1][j-1] == "@": neighbours += 1
        if neighbours < 4: 
          total += 1
          new_grid[i][j] = "."
    grid = new_grid
    grand_total += total
  return grand_total

def get(filename):  
  with open(filename, 'r') as f:
    return [list(line.strip()) for line in f]

print(accessible_paper_rolls(get('test')))
print(accessible_paper_rolls(get('input')))
