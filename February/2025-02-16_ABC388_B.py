import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue整理
# N D 蛇の数 出力する行数
# TL 蛇ごとの情報をリストで持つ
# 蛇重さは太さと長さの積（Dの長さがk伸びる）
# k行目のループで各蛇の重さを計算し、maxの蛇の重さをprint

# レビュー指摘
# 変数名を理解しやすい形に変更
# リスト内包表記を使用し可読性向上

N, D = map(int, input().split())
snakes = [list(map(int, input().split())) for _ in range(N)]

for k in range(1, D+1):
    weights = [thickness * (length + k) for thickness, length in snakes]
    print(max(weights))
    # calc_arr = []
    # for a in range(len(snakes)):
    #     calc_arr.append((snakes[a][1] + i) * snakes[a][0])
    # print(max(calc_arr))


# AIの別解
# import numpy as np

# N, D = map(int, input().split())
# snakes = np.array([list(map(int, input().split())) for _ in range(N)])

# # 太さと長さを分離
# thicknesses = snakes[:, 0]  # 全蛇の太さ
# lengths = snakes[:, 1]      # 全蛇の長さ

# # 各kに対して一括計算
# for k in range(1, D+1):
#     weights = thicknesses * (lengths + k)
#     print(np.max(weights))

# N, D = map(int, input().split())
# snakes = []
# max_thickness = 0  # 最大の太さを記録
# max_length = 0     # 最大の長さを記録

# for _ in range(N):
#     t, l = map(int, input().split())
#     snakes.append((t, l))
#     max_thickness = max(max_thickness, t)
#     max_length = max(max_length, l)

# # 最大の太さを持つ蛇が常に最大重量になる可能性が高い
# for k in range(1, D+1):
#     max_weight = 0
#     for thickness, length in snakes:
#         weight = thickness * (length + k)
#         max_weight = max(max_weight, weight)
#     print(max_weight)

# import heapq

# N, D = map(int, input().split())
# snakes = [list(map(int, input().split())) for _ in range(N)]

# for k in range(1, D+1):
#     # -1を掛けることで最大値を取得できる
#     weights = [-1 * (t * (l + k)) for t, l in snakes]
#     heapq.heapify(weights)
#     print(-1 * weights[0])  # 最大値を出力