N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    ok = True
    for j in range(1, M+1):
        if j in A:
            continue
        else:
            ok = False
    if ok:
        del A[-1]
        ans += 1
    else:
        break
print(ans)