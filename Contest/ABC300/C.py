import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 二重ループ(O(NM))の処理①
# grid[i][v:v+3] == ['#','.','#']ならvisited[i][v] = 1を設定
# `#`の右下が`#`かどうか判定
# 上記がTrueなら左上or右上の`#`の個数を計算する

H, W = list(map(int, input().split()))
N = [0] * min(H, W) + [0]

grid = [list(str(input())) for _ in range(H)]

# まずはサイズ1になりうる記号箇所の左上の頂点をマッピング

visited = [[0] * W for _ in range(H)]
for i in range(H):
    for v in range(W):
        if grid[i][v:v+3] == ['#','.','#'] and (v < 2 or visited[i][v-2] != 1):
            if i < 1 or visited[i-2][v] != 1:
                visited[i][v] = 1

N[1] = visited[0].count(1)

# visited[i][v] == 1がTrueなら、grid[i-1][v-1] == '#'か判定

for i in range(1, H-2):
    for v in range(W-2):
        if visited[i][v] == 1:
            # print(f'共通処理(条件分岐後) >>> i:{i}/v:{v}')
            size = 1
            # 起点から左上が'#'かを検証していく
            for c in range(1, min(i, v)+1):
                if grid[i-c][v-c] == '#':
                    size += 1
                    # print(f'i:{i}/v:{v}/c:{c}/size:{size}')
                elif grid[i-c][v-c] == '.':
                    break
            # print(f'sizeは{size}')
            N[size] += 1

print(*N[1:])


# AIの解説
# H, W = visited(int, input().split())
# C = [list(input()) for _ in range(H)]

# N = min(H, W)  # 最大のバツ印のサイズ
# result = [0] * N  # 各サイズのカウント

# # 斜めの4方向 (dx, dy)
# directions = [(-1,-1), (-1,1), (1,-1), (1,1)]

# # 全ての `#` マスを中心候補として確認
# for i in range(H):
#     for j in range(W):
#         if C[i][j] != '#':
#             continue  # `#` でないならスキップ

#         size = 0
#         # 外側へサイズを伸ばしていく
#         while True:
#             size += 1
#             ok = True
#             for dx, dy in directions:
#                 ni = i + dx * size
#                 nj = j + dy * size
#                 if not (0 <= ni < H and 0 <= nj < W and C[ni][nj] == '#'):
#                     ok = False
#                     break  # 1方向でも満たさないと終了
#             if not ok:
#                 size -= 1  # 最後の失敗分のサイズを戻して終了
#                 break

#         if size >= 1:
#             result[size - 1] += 1  # サイズは1-indexedなので調整

# print(*result)
