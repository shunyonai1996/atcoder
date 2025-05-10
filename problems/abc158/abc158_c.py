a, b = map(int, input().split())

ans = -1
for i in range(1, 10 ** 5):
    if i * 8 // 100 == a and i * 10 // 100 == b:
        ans = i
        break
print(ans)