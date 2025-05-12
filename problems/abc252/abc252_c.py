N = int(input())
S = [list(map(int, input())) for _ in range(N)]
min_t = float('inf')

for i in range(10):
    t = 0
    for s in S:
        t += s.index(i)
    min_t = min(t, min_t)
print(min_t)