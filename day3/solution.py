def argmax(s, low, high):
  return low + max(range(len(s[low:high])), key=lambda i: s[low:high][i])

def flip_batteries(banks, n=12):
  total = 0
  for bank in banks:
    num = ""
    low = 0
    high = len(bank)+1-n
    for _ in range(n):
      i = argmax(bank, low, high)
      num += bank[i]
      low = i+1
      high += 1
    total += int(num)
  return total

def get(filename):  
  with open(filename, 'r') as f:
    return [line.strip() for line in f]

print(flip_batteries(get('test')))
print(flip_batteries(get('input')))
