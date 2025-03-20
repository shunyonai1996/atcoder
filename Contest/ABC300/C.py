import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# 2回目

H, W = list(map(int, input().split()))
C = [list(str(input())) for _ in range(H)]

ans = [0] * min(H,W)
for i in range(1, H-1):
    for j in range(1, W-1):
        if C[i][j] == '#':
            size = -1
            for k in range(1, min(W-1, H-1)):
                if C[i-k][j-k] == '#' and C[i+k][j+k] == '#' and C[i-k][j+k] == '#' and C[i+k][j-k] == '#':
                    size += 1
                else:
                    break
            if 0 <= size: ans [size] += 1
print(*ans)


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
