N, K = map(int, input().split())
A = list(map(int, input().split()))

num = 1
for i in range(N):
    num *= A[i]
    if num < 10 ** K:
        continue
    else:
        num = 1
print(num)