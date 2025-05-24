X, Y = map(int, input().split())
cnt = 0

for i in range(1, 7):
    for j in range(1, 7):
        if X <= i + j:
            cnt += 1
        elif Y <= abs(i - j):
            cnt +=1

print(cnt / (6 * 6))