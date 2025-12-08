def split_beams(lines):
  beams = [1 if c == "S" else 0 for c in lines[0]]
  for line in lines[1:]:
    new_beams = [0] * len(line)
    for i, c in enumerate(line):
      if c == "." and beams[i]:
        new_beams[i] = beams[i]
    for i, c in enumerate(line):
      if c == "^" and beams[i]:
        if i > 0: new_beams[i-1] += beams[i]
        if i < len(line)-1: new_beams[i+1] += beams[i]
    beams = new_beams
  return sum(beams)

def get(filename):
  with open(filename, 'r') as f:
    return [line.strip() for line in f]
  
print(split_beams(get('test')))
print(split_beams(get('input')))
