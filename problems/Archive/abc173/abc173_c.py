import itertools
H, W, K = map(int, input().split())
grid = [list(input()) for _ in range(H)]
ans = 0

default_blk = 0
for c in grid:
    default_blk += c.count('#')
if default_blk == K:
    ans += 1

new_grid = [list([0] * H) for _ in range(W)]
for i in range(H):
    if default_blk - grid[i].count('#') == K:
        ans += 1
    for j in range(W):
        new_grid[j][i] = grid[i][j]

for i in range(W):
    if default_blk - new_grid[i].count('#') == K:
        ans += 1

for v in itertools.combinations(grid, 2):
    cnt = 0
    for l in v:
        cnt += l.count('#')
    if default_blk - cnt == K:
        print(v)
        ans += 1


for v in itertools.combinations(new_grid, 2):
    cnt = 0
    for l in v:
        cnt += l.count('#')
        print(v)
    if default_blk - cnt == K:
        ans += 1


for i in range(H):
    for j in range(W):
        if default_blk - grid[i].count('#') - new_grid[j].count('#') == K:
            ans += 1



print(ans)