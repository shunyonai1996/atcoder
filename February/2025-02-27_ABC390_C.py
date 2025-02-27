import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 連続したリストから四角の判定をする方法検討
# `.`によって四角を作れない事象検証

# 1行内での検証
# `#`の間に`.`があったらNo
# `#`の間が`?`か`#`ならYes
# 最初に`#`が現れた時に塗りつぶす必要のあるインデックスをリストで保存

# 前の行から正方形を作れるか

# ×NGの行があった場合、処理を終了

H,W = list(map(int, input().split()))

check_list = [0] * W
flg = False
cnt = 0

for i in range(H):
    S = list(*input().split())
    if flg == False and '#' in S:
        flg = True
        for i, name in enumerate(S):
            if name == '#' or name == '?':
                check_list[i] = 1
    elif flg:
        for i, value in enumerate(check_list):
            if check_list[value] == 1 and (S[i] == '#' or S[i] == '?'):
                continue
            elif check_list[value] == 0 and (S[i] == '#'):
                print('No')
                break


# AIによる回答
def solve(H, W, grid):
    # 黒マスの座標を記録
    black = []
    min_i = H
    max_i = -1
    min_j = W
    max_j = -1

    # 黒マスの範囲を特定
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                black.append((i, j))
                min_i = min(min_i, i)
                max_i = max(max_i, i)
                min_j = min(min_j, j)
                max_j = max(max_j, j)
    # 黒マスがない場合
    if not black:
        return 'Yes'

    # 長方形の領域をチェック
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if grid[i][j] == '.':  # 白マスがあれば不可能
                return 'No'

    # 長方形の外に黒マスがないか確認
    for i, j in black:
        if not (min_i <= i <= max_i and min_j <= j <= max_j):
            return 'No'

    return 'Yes'

# 入力処理
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
print(solve(H, W, grid))

# 解説記事のPython変換コード
# 入力
H, W = map(int, input().split())
S = [input() for _ in range(H)]

# 初期化
h_min = W   # C++の1000に相当（十分大きい値）
h_max = -1
w_min = W   # C++の1000に相当（十分大きい値）
w_max = -1
flag = True

# バウンディングボックスの座標を見つける
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            h_min = min(h_min, i)
            h_max = max(h_max, i)
            w_min = min(w_min, j)
            w_max = max(w_max, j)

# バウンディングボックス内に'.'があるかチェック
for i in range(h_min, h_max + 1):
    for j in range(w_min, w_max + 1):
        if S[i][j] == '.':
            flag = False

# 結果出力
print("Yes" if flag else "No")