N, K = map(int, input().split())
a = list(map(int, input().split()))

sort_a = sorted(a)

b = [[] for _ in range(K)]
for i in range(N):
    b[i % K].append(a[i])

for i in range(K):
    b[i].sort()

na = []
idx = [0] * K
for i in range(N):
    r = i % K
    na.append(b[r][idx[r]])
    idx[r] += 1

print("Yes" if na == sort_a else "No")
