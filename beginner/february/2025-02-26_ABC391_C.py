import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 移動した鳩の情報の保持方法
# 鳩/巣が1/1の場合、変数保持しない
# Q回のループでクエリを処理する

# N, Q = list(input().split())
# pos = [i for i in range(1, int(N)+1)]
# cnt = [1 for _ in range(int(N))]
# ans = 0

# for _ in range(int(Q)):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         # 移動元の巣の数を-1
#         cnt[pos[query[1]-1]-1] -= 1
#         # 移動先の巣の数を+1
#         cnt[query[2]-1] += 1
#         # 鳩に対応する巣の値を書き換える
#         pos[query[1]-1] = query[2]
#         # 移動した巣の数が2以上なら+1
#         ans += 1 if cnt[query[2]-1] > 1 else -1
#     else:
#         print(ans)

# 解説によるヒント
# ループごとにフルスキャンするとO(N^2)
# 鳩[i] いる巣の番号
# cnt[i] 巣[i]にいる鳩の羽数
# ans 回答を差分で保持する


# 解答例
N, Q = map(int, input().split())
ans = 0
# リストの0番目を欠番にすることでindexと巣の番号が一致する
cnt = [0] + [1] * N
# rangeのstopを要素数+1にすることでindexと鳩の番号が一致する
pos = list(range(N + 1))
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        P, H = query[1:]
        # 鳩 P は移動する前は巣 pos[P] にいる
        # 鳩 P が移動することで 巣 pos[P] にいる鳩の数が 2 から 1 に減る場合, ans を 1 減らす
        if cnt[pos[P]] == 2:
            ans -= 1
        # 巣 pos[P] の鳩の数を 1 減らす
        cnt[pos[P]] -= 1

        # 鳩 P がいる巣を H に変更する
        pos[P] = H
        # 巣 H の鳩の数を 1 増やす
        cnt[pos[P]] += 1
        # 鳩 P が移動することで 巣 H にいる鳩の数が 1 から 2 に増える場合，ans を 1 増やす
        if cnt[pos[P]] == 2:
            ans += 1
    else:
        print(ans)