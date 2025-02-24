import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# Qのi番目のインデックス検索
# インデックス番目のPの番号を検索
# 検索した番号-1番目のQの要素をリストに追加
# 上記をループ実行

N = int(input())
Q = list(map(int, input().split()))
P = list(map(int, input().split()))
answer = ''

for i in range(1, N+1):
    answer = ' '.join([answer, str(P[Q[P.index(i)]-1])])

print(answer)