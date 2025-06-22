N, X = map(int, input().split())
A = map(int, input().split())

ans = []
for i in A:
    if i != X:
        ans.append(i)

print(" ".join(map(str, ans)))