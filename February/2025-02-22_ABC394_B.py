import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 入力をリストに格納
# ソートで文字列の長さが小さい順に並べ替える
# ループでリストの要素を文字結合

n = int(input())
arr = [input() for _ in range(n)]

arr_copy = sorted(arr, key=len)

answer = ''
for i in range(n):
    answer += arr_copy[i]

print(answer)