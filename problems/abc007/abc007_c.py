from collections import deque

# デバッグ用表示関数
def print_debug(current, q_state):
    print(f"現在位置: {current} キュー: {list(q_state)}")
    for row in distance:
        print(' '.join(f"{x:2}" for x in row))
    print("---")

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy -= 1; sx -= 1; gy -= 1; gx -= 1

maze = [input().strip() for _ in range(R)]
distance = [[-1]*C for _ in range(R)]
distance[sy][sx] = 0


q = deque()  # 変数名qで正しく初期化
q.append((sy, sx))

# print(maze)
# print(distance)
# print(q)

directions = [(-1,0), (0,1), (1,0), (0,-1)]

# 処理ループ（デバッグ版）
while q:
    current = q.popleft()
    print_debug(current, q)

    i, j = current
    if (i, j) == (gy, gx):
        break

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C:
            if maze[ni][nj] == '.' and distance[ni][nj] == -1:
                distance[ni][nj] = distance[i][j] + 1
                q.append( (ni, nj) )

print(f"答え: {distance[gy][gx]}")
print(distance[gy][gx])
