def merge_overlapping_ranges(ranges):
  out = []
  i = 0
  while i < len(ranges):
    start = ranges[i][0]
    end = ranges[i][1]
    while i < len(ranges)-1 and end + 1 >= ranges[i+1][0]:
      end = max(end, ranges[i+1][1])
      i += 1
    out.append((start, end))
    i += 1
  return out

def preprocess_ranges(ranges):
  out = []
  for id_range in ranges:
    low, high = map(int, id_range.split("-"))
    out.append((low, high))
  out.sort(key=lambda x: x[0])
  return merge_overlapping_ranges(out)

def fresh_ingredients(input):
  ranges, ingredients = input
  ranges = preprocess_ranges(ranges)
  total = 0
  for ingredient in ingredients:
    for id_range in ranges:
      if ingredient >= id_range[0] and ingredient <= id_range[1]:
        total += 1
        break
  return total

def fresh_ranges(input):
  ranges, _ = input
  total = 0
  for id_range in preprocess_ranges(ranges):
    total += (id_range[1] - id_range[0]) + 1
  return total

def get(filename):  
  with open(filename, 'r') as f:
    lines = [line.strip() for line in f]
    sep = lines.index("")
    return lines[:sep], [int(x) for x in lines[sep+1:]]

print(fresh_ranges(get('test')))
print(fresh_ranges(get('input')))
