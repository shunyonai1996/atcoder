N = int(input())
P = map(int, input().split())
min_val = float('inf')
ans = 0

for v in P:
    if v < min_val:
        min_val = v
        ans += 1

print(ans)