import numpy as np

def connect_boxes(circuits, i, j):
  idx_i = -1
  idx_j = -1
  for index, circuit in enumerate(circuits):
    if i in circuit: idx_i = index
    if j in circuit: idx_j = index
  if idx_i != -1 and idx_j != -1:
    if idx_i == idx_j: 
      return
    circuits[idx_i].update(circuits[idx_j])
    circuits.pop(idx_j)
  elif idx_i != -1:
    circuits[idx_i].add(j)
  elif idx_j != -1:
    circuits[idx_j].add(i)
  else:
    circuits.append({i, j})

def connect_junction_boxes(x):
  N = x.shape[0]
  distances = []
  for i in range(N):
    for j in range(i + 1, N):
      distances.append([np.linalg.norm(x[i] - x[j]), i, j])
  distances.sort(key=lambda x: x[0])
  circuits = []
  for it in range(len(distances)):
      i, j = distances[it][1], distances[it][2]
      connect_boxes(circuits, i, j)
      if len(circuits) == 1 and len(circuits[0]) == N:
        return x[i][0] * x[j][0]
  return 0

def get(filename):
  with open(filename, 'r') as f:
    return np.array([line.strip().split(",") for line in f]).astype(float)
  
print(connect_junction_boxes(get('test')))
print(connect_junction_boxes(get('input')))
