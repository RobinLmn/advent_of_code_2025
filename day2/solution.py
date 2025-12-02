def find_invalid_ids(ids):
  total = 0
  for id_range in ids:
    low, high = map(int, id_range.split('-'))
    for id in range(low, high+1):
      id_str = str(id)
      if id_str in (id_str + id_str)[1:-1]:
        total += id
  return total

def test(testcase, answer):
  output = find_invalid_ids(testcase)
  print(f"Output: {output}\t Expected: {answer}")

def get(filename):  
  with open(filename, 'r') as f:
    return f.read().split(',')

test(get('test'), 0)
print(find_invalid_ids(get('input')))
