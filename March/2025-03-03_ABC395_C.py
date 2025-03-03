import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# ダブりが存在するかどうかを検証
# カウントアップしていき、重複が存在した時点の長さを保持
# ダブってる数値を洗い出す
# その中の距離が最小の長さを求める

N = int(input())
A = list(map(int, input().split()))

print(N, A)

dup_list = {i:v for i, v in enumerate(A) if A.count(v) > 1}


# AIによる解説
# 尺取り法使用
# 入力処理
N = int(input().strip())
A = list(map(int, input().split()))

# 必要な変数を準備
seen = {}  # 各要素の出現回数を記録する辞書
l = 0      # 左端
min_length = float('inf')  # 最小長を記録（初期値は∞）

# 右端をスライドさせる
for r in range(N):
    seen[A[r]] = seen.get(A[r], 0) + 1  # 新しい要素を追加
    print(seen)

    # もし同じ要素が2回以上出現したら、条件を満たすので左端を動かして調整
    while seen[A[r]] > 1:
        print(A[r])
        print(r, l)
        min_length = min(min_length, r - l + 1)
        print(min_length)
        seen[A[l]] -= 1
        l += 1  # 左端を進めて部分列を短縮

# 結果の出力
print(min_length if min_length != float('inf') else -1)