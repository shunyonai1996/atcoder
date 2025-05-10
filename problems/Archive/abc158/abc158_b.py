n, a, b = map(int, input().split())

if a == 0:
    print(0)
else:
    ans = n // (a + b) * a
    ans += a if a < n % (a + b) else n % (a + b)
    print(ans)