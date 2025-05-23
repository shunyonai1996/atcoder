X, N = map(int, input().split())
if 0 < N:
    P = list(map(int, input().split()))
else:
    print(X)
    exit()

nums = [i for i in range(0, 102) if i not in P]
diff = 102
ans = -1
for i in nums:
    if min(abs(X - i), diff) < diff:
        diff = min(abs(X - i), diff)
        ans = i
print(ans)