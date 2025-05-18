A, B, C, K = [i for i in map(int, input().split())]

ans = 0
for i in range(1, K + 1):
    if i <= A:
        ans += 1
    elif i - A <= B:
        continue
    else:
        ans -= 1
print(ans)