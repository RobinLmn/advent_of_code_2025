import numpy as np

def find_largest_rectangle(x):
  N = x.shape[0]
  edges = []
  for i in range(N):
    edges.append((x[i], x[(i+1)%N]))
  max_area = 0
  for i in range(N):
    for j in range(i + 1, N):
      x_min, x_max = min(x[i][0], x[j][0]), max(x[i][0], x[j][0])
      y_min, y_max = min(x[i][1], x[j][1]), max(x[i][1], x[j][1])
      area = (x_max - x_min + 1) * (y_max - y_min + 1)
      if area < max_area:
        continue
      # check if the area contains red tiles
      mask = ((x[:, 0] > x_min) & (x[:, 0] < x_max) & (x[:, 1] > y_min) & (x[:, 1] < y_max))
      if np.any(mask):
          continue
      # check edge intersections
      edge_intersects = False
      for p1, p2 in edges:
          if p1[0] == p2[0]: 
              edge_x = p1[0]
              if x_min < edge_x < x_max:
                  if min(p1[1], p2[1]) <= y_min and max(p1[1], p2[1]) >= y_max:
                      edge_intersects = True
                      break
          elif p1[1] == p2[1]:
              edge_y = p1[1]
              if y_min < edge_y < y_max:
                  if min(p1[0], p2[0]) <= x_min and max(p1[0], p2[0]) >= x_max:
                      edge_intersects = True
                      break
      if edge_intersects:
        continue
      # check center is inside the polygon
      mid_x, mid_y= (x_min + x_max) / 2, (y_min + y_max) / 2
      intersections = 0
      for p1, p2 in edges:
        e_y_min, e_y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
        if e_y_min < mid_y < e_y_max and p1[0] > mid_x:
          intersections += 1
      if intersections % 2 == 1:
        max_area = area
  return max_area

def get(filename):
  with open(filename, 'r') as f:
    return np.array([line.strip().split(",") for line in f]).astype(int)
  
print(find_largest_rectangle(get('test')))
print(find_largest_rectangle(get('input')))
