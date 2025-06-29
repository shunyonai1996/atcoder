import math

A, B, W = map(int, input().split())
W *= 1000

# 論理的に厳密な範囲計算
# 最小個数: 重い橙(B)を使った場合 → ceil(W/B)
# 最大個数: 軽い橙(A)を使った場合 → floor(W/A)
min_possible = math.ceil(W / B)
max_possible = W // A

min_val = float('inf')
max_val = float('-inf')

for n in range(min_possible, max_possible + 1):
    if A * n <= W and W <= B * n:
        min_val = min(min_val, n)
        max_val = max(max_val, n)

if min_val == float('inf') and max_val == float('-inf'):
    print('UNSATISFIABLE')
else:
    print(min_val, max_val)