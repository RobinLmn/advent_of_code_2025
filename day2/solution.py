def find_invalid_ids(ids):
  total = 0
  for id_range in ids:
    low, high = map(int, id_range.split('-'))
    for id in range(low, high+1):
      id_str = str(id)
      if id_str in (id_str + id_str)[1:-1]:
        total += id
  return total

def get(filename):  
  with open(filename, 'r') as f:
    return f.read().split(',')

print(find_invalid_ids(get('test')))
print(find_invalid_ids(get('input')))
