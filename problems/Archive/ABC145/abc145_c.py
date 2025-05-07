import math
import itertools

N = int(input())
towns = [tuple(map(int, input().split())) for _ in range(N)]

total_distance = 0
avg_val = 0

for path in itertools.permutations(towns):
  distance = 0
  for j in range(N-1):
    x1, y1 = path[j]
    x2, y2 = path[j+1]
    distance += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
  total_distance += distance
  avg_val += 1

average = total_distance / avg_val
print(f"{average:.10f}")