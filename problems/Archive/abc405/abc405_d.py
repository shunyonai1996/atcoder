from collections import deque

# 正しい入力処理（H行W列のグリッドを読み取る）
H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]
print(f"入力グリッド: {grid}")

# 非常口の座標を収集
q = deque()
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'E':
            q.append((i, j))
            print(f"非常口追加: ({i}, {j})")

directions = [(-1,0, 'v'), (0,1, '<'), (1,0, '^'), (0,-1, '>')]

print("\nBFS開始:")
step = 0
while q:
    print(f"\nステップ {step}: キューサイズ {len(q)}")
    for _ in range(len(q)):
        i, j = q.popleft()
        print(f"処理中: ({i},{j}) 現在の値: {grid[i][j]}")

        for di, dj, arrow in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W:
                if grid[ni][nj] == '.':
                    grid[ni][nj] = arrow
                    q.append((ni, nj))
                    print(f" 更新: ({ni},{nj}) → {arrow} を追加")
    step += 1

print("\n最終結果:")
for row in grid:
    print(''.join(row))
