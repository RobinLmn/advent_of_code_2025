import numpy as np

def solve_homework(problems):
  total = 0
  for problem in problems:
    op = problem[-1]
    nums = np.array(problem[:-1]).astype(int)
    if op == "*":
      total += nums.prod()
    if op == "+":
      total += nums.sum()
  return total

def get(filename):
  with open(filename, 'r') as f:
    lines = [line[:-1] for line in f]
    max_len = max(len(line) for line in lines)
    out = [[]]
    for i in range(max_len):
      num = ""
      for line in lines:
        if len(line)-1 < i or line[i] == " " or not line[i].isnumeric():
          continue
        num += line[i]
      if num == "":
        out.append([])
      else:
        out[-1].append(num)
    for i, op in enumerate(lines[-1].split()):
      out[i].append(op)
    return out
  
print(solve_homework(get('test')))
print(solve_homework(get('input')))
