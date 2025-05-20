N = int(input())
A = list(map(int, input().split()))

ans = A[0]
for i in range(1, N):
    ans *= A[i]

print(ans) if ans <= 10 ** 18 else print('-1')