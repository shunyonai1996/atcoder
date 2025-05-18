N, M, X = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(N)]

min_cost = -1

for bit in range(1 << N):
    cost = 0
    skill = [0] * M
    for i in range(N):
        if bit & (1 << i):
            cost += books[i][0]
            for j in range(M):
                skill[j] += books[i][j + 1]
    if all(s >= X for s in skill):
        if min_cost == -1 or cost < min_cost:
            min_cost = cost

print(min_cost)
