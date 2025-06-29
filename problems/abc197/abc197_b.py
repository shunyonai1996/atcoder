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

# typescriptっぽく
# # 下方向
# i = X
# while i < H and grid[i][Y-1] != '#':
#     cnt += 1
#     i += 1

# # 上方向
# i = X - 2
# while i >= 0 and grid[i][Y-1] != '#':
#     cnt += 1
#     i -= 1

# # 右方向
# j = Y
# while j < W and grid[X-1][j] != '#':
#     cnt += 1
#     j += 1

# # 左方向
# j = Y - 2
# while j >= 0 and grid[X-1][j] != '#':
#     cnt += 1
#     j -= 1

print(cnt)