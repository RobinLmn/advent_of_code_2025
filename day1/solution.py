def crack_password(moves, dial=50, N=100):
  loops = 0
  for dir, delta in moves:
    new_dial = dial + (delta if dir == "R" else -delta)
    if dir == "R":
      loops += (new_dial // N) - (dial // N)
    else:
      loops += ((dial - 1) // N) - ((new_dial - 1) // N)
    dial = new_dial
  return loops

def test(testcase, answer):
  output = crack_password(testcase)
  print(f"Output: {output}\t Expected: {answer}")

def get(filename):  
  with open(filename, 'r') as f:
    return [(line[0], int(line[1:])) for line in f]

test([["R", 60]], 1)
test([["L", 60]], 1)
test([["R", 160]], 2)
test([["L", 160]], 2)
test([["L", 50]], 1)
test([["L", 50], ["L", 1]], 1)
test([["R", 50]], 1)
test([["R", 1000]], 10)
test([["R", 1000], ["L", 50], ["L", 1]], 11)
test(get('test'), 6)
print(crack_password(get('input')))
