N, M = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)

ans = 'Yes'
total = sum(A)
for i in A[:M]:
    if i < total * (1 / (4 * M)):
        ans = 'No'

print(ans)