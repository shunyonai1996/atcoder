n, m = map(int, input().split())
sc = [list(map(int, input().split())) for i in range(m)]

for s,c in sc:
    if 1 < n and s == 1 and c == 0:
        print('-1')
        exit()

ans = '-1'
for i in range(0, 1000):
    v = str(i)
    check = True
    if len(v) != n:
        continue
    for j in range(m):
        s, c = sc[j]
        if v[s-1] != str(c):
            check = False
            break
    if check:
        ans = v
        break
print(ans)