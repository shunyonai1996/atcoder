A, B, X = map(int, input().split())

low = 1
high = 10**9
max_n = 0

while low <= high:
    mid = (low + high) // 2
    d = len(str(mid))
    cost = A * mid + B * d

    if cost <= X:
        max_n = mid
        low = mid + 1  # より大きい値を探索
    else:
        high = mid - 1  # 条件を満たさないので範囲を狭める

print(max_n)
