H, W, X, Y = map(int, input().split())

grid = [input() for _ in range(H)]
cnt = 1

for i in range(X, H):
    if grid[i][Y-1] == '#':
        break
    cnt += 1

for i in range(X-2, -1, -1):
    if grid[i][Y-1] == '#':
        break
    cnt += 1

for j in range(Y, W):
    if grid[X-1][j] == '#':
        break
    cnt += 1

for j in range(Y-2, -1, -1):
    if grid[X-1][j] == '#':
        break
    cnt += 1

print(cnt)