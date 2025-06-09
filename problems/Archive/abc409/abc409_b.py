N = int(input())
A = sorted(list(map(int, input().split())))

ans = 0
max_cnt = 0
for i in range(N+1):
    cnt = 0
    for j in A:
        if i <= j:
            cnt += 1
    if i <= cnt:
        ans = i
        max_cnt = cnt

print(ans)