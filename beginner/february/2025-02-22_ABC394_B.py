import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 入力をリストに格納
# ソートで文字列の長さが小さい順に並べ替える
# ループでリストの要素を文字結合

# AIによるソースレビュー
# 変数名を適切に設定
# 出力にはjoinを使う

n = int(input())
strings = [input() for _ in range(n)]

sorted_strings = sorted(strings, key=len)

answer = ''.join(sorted_strings)

print(answer)


# AIによる別解
import heapq

n = int(input())
# (長さ, 文字列)のタプルをヒープに格納
heap = [(len(s := input()), s) for _ in range(n)]
heapq.heapify(heap)

# ヒープから順に取り出して結合
answer = ''.join(heapq.heappop(heap)[1] for _ in range(n))
print(answer)