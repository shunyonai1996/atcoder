import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# AIによるソースレビュー
# listよりもsetのほうが高速（検索にハッシュテーブル使用する）
# -> `not in S`でO(1)で検索できる※リストはO(N)
# ループを内包表記で記述
# 値が1つ以上あるかのチェックは比較演算子が不要

N, M = map(int, input().split())
S = set(map(int, input().split()))
ans = [i for i in range(1,N+1) if i not in S]

print(len(ans))
if ans:
    print(*ans)