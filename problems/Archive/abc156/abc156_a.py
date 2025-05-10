n, r = map(int, input().split())

print(r) if 10 <= n else print(r + 100 * (10 - n))