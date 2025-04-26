import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
P = list(map(int, input().split()))
ans_list = [0] * N
rank = 0

for i in range(N):
    if max(P) == 0: break
    # 最高得点者をカウント -> 複数人の場合
    if 1 < P.count(max(P)):
        # 最高得点者の人数
        cnt_top_rankers = P.count(max(P))
        # 最高得点者の人数分ループを回す
        for l in range(cnt_top_rankers):
            # 最高得点者を回答用のリストに順位を追加
            ans_list[P.index(max(P))] = rank + 1
            # カウント済みの得点者の点数を0に更新
            P[P.index(max(P))] = 0
        # 最高得点者の人数分rankを増やす
        rank += cnt_top_rankers
    # 最高得点者が1人
    else:
        # 最高得点者を回答用のリストに順位を追加
        top_ranker = P.index(max(P))
        # カウント済みの得点者の点数を0に更新
        P[P.index(max(P))] = 0
        ans_list[top_ranker] = rank + 1
        rank += 1

[print(i) for i in ans_list]

# 別解
# P[i]よりも大きい得点者の数をカウント
N = int(input())
P = list(map(int, input().split()))

for i in range(N):
    rank = 1
    for j in range(N):
        if P[i] < P[j]:
            rank += 1
    print(rank)

# AIによる別解
n = int(input())
p = list(map(int, input().split()))

indexed = sorted([(v, i) for i, v in enumerate(p)], reverse=True)
res = [0] * n
rank = 1
for i, (val, idx) in enumerate(indexed):
    if i > 0 and val == indexed[i - 1][0]:
        print(f'i:{i}/val:{val}/idx:{idx}')
        res[idx] = res[indexed[i - 1][1]]
    else:
        print(f'i:{i}/val:{val}/idx:{idx}')
        print(f'res[idx]:{res}')
        res[idx] = i + 1
        print(f'res[idx]:{res}')

for r in res:
    print(r)