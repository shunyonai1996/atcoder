A, B, W = map(int, input().split())
W *= 1000
min_val = float('inf')
max_val = float('-inf')

for n in range(1, W//A+1):
    if A * n <= W and W <= B * n:
        min_val = min(min_val, n)
        max_val = max(max_val, n)

if min_val == float('inf') and max_val == float('-inf'):
    print('UNSATISFIABLE')
else:
    print(min_val, max_val)