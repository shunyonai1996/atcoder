import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# Qのi番目のインデックス検索
# インデックス番目のPの番号を検索
# 検索した番号-1番目のQの要素をリストに追加
# 上記をループ実行

# AIによるソースレビュー
# indexの使用により、O(N^2)の計算量
# 辞書テーブルを作成
# joinは最後に一度のみ使用する

N = int(input())
Q = list(map(int, input().split()))
P = list(map(int, input().split()))

P_index = {value: index for index, value in enumerate(P)}
ans_list = [str(P[Q[P_index[i]]-1]) for i in range(1, N+1)]

print(' '.join(ans_list))


# AIによる別解
# 辞書ではなく配列でインデックスを管理する
# メモリ効率が若干向上する
N = int(input())
Q = list(map(int, input().split()))
P = list(map(int, input().split()))

# Pの各値の位置を記録する配列
pos = [0] * (N + 1)
for i in range(N):
    pos[P[i]] = i

# 結果を求める
result = []
for i in range(1, N + 1):
    person_pos = pos[i]      # i番の人の位置
    looking_at = Q[person_pos]  # その人が見ている人の番号
    result.append(str(P[looking_at - 1]))

print(' '.join(result))