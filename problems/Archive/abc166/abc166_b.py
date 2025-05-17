N, K = map(int, input().split())

A = []
for i in range(K):
    d = int(input())
    A += [i for i in map(int, input().split())]

ans = 0
for i in range(1, N+1):
    if i not in set(A):
        ans += 1
print(ans)