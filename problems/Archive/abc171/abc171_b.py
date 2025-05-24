N, K = map(int, input().split())
P = sorted(map(int, input().split()))

ans = 0
for i in range(K):
    ans += P[i]

print(ans)