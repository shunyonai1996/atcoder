N, M = map(int, input().split())
A = sum(map(int, input().split()))

print('-1') if N < A else print(N-A)