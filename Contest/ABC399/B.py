import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
P = list(map(int, input().split()))
ans_list = [0] * N
rank = 0

for i in range(N):
    count_top_ranker = max(P)
    if count_top_ranker == 0: break
    if 1 < P.count(count_top_ranker):
        # print(f'1回目{P.count(count_top_ranker)}')
        rank_add = P.count(count_top_ranker)
        for l in range(P.count(count_top_ranker)):
            multi_top_ranker = P.index(max(P))
            ans_list[multi_top_ranker] = rank + 1
            P[P.index(max(P))] = 0
        rank += rank_add
        # print(f'2回目{rank_add}')
        # print(rank)
    else:
        top_ranker = P.index(max(P))
        P[P.index(max(P))] = 0
        ans_list[top_ranker] = rank + 1
        rank += 1

[print(i) for i in ans_list]