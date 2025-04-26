import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 各グリッドに入るリストを準備
# 入力と一致する値をリストから全て除外
# 除外後、リスト内の要素を全て足し合わせる

# AIのレビュー
# 一時的なリストの作成のため、メモリを余分に使用

X = int(input())
grid = [i*j for j in range(1,10) for i in range(1,10)]
total = sum([grid[i] for i in range(0, len(grid)) if X != grid[i]])

print(total)

# AIの別解1
# ... existing code ...
# X = int(input())
# リスト変換を挟まず、ワンラインで完結
# 9*9のグリッドが不要だから、メモリ効率が良い
# total = sum(i * j for i in range(1, 10) for j in range(1, 10) if i * j != X)
# print(total)

# AIの別解2
# 変数名を絞っている
# 中間結果としてリストやタプルを持たないため、メモリ効率が良い
# ... existing code ...
# X = int(input())
# total = 0
# for i in range(1, 10):
#     for j in range(1, 10):
#         product = i * j
#         if product != X:
#             total += product
# print(total)