N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
max_val = max(A)
ans = 'No'

for i in B:
    if A[i-1] == max_val:
        ans = 'Yes'

print(ans)