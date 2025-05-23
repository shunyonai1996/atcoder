N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in L:
    if A[i-1] == N:
        continue
    if A[i-1] + 1 not in A:
        A[i-1] += 1

print(' '.join(map(str, A)))