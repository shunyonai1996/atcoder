N = int(input())
ans = float('inf')

for i in range(N):
    A, P, X = map(int, input().split())
    if A < X:
        ans = min(ans, P)

print(-1) if ans == float('inf') else print(ans)