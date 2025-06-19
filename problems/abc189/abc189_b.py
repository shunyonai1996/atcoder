N, X = map(int, input().split())
alcohol = 0

for i in range(N):
    v, p = map(int, input().split())
    alcohol += v * p / 100
    if X < alcohol:
        print(i + 1)
        exit()

print(-1)