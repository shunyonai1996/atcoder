X = int(input())
ans = 0
y = 100
while True:
    y = y * 101 // 100
    ans += 1
    if X <= y:
        print(ans)
        exit()