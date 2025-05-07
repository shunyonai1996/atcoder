N, K, M = list(map(int, input().split()))
A = sum(map(int, input().split()))

ans = -1
for i in range(K+1):
    if M * N <= (A + i):
        ans = i
        break

print(ans)