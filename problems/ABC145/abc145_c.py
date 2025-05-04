import math
import itertools

N = int(input())
# math.sqrt()
map_list = [[0, 0] for _ in range(N)]
for i in range(N):
  map_list[i][0],map_list[i][1] = map(int, input().split())
print(map_list)
_permutations = list(itertools.permutations(map_list, 3))

max_distance = 0

print(_permutations)
for i in range(len(_permutations)):
  distance = 0
  for j in range(N):
    for l in range(N):
      distance_x = (_permutations[i][j][0] - _permutations[i][j][1]) ** 2
      distance_y = (_permutations[i][j][0] - _permutations[i][j][1]) ** 2
      distance += math.sqrt(distance_x+distance_y)
      print(f"distance_x: {distance_x}, distance_y: {distance_y}, distance: {distance}")
  avg_distance = distance / len(_permutations)
  max_distance = max(max_distance, avg_distance)
print(max_distance)