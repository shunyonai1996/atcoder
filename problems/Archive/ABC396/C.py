import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# AIによるソースレビュー
# current_ans = current_ans + B[i]はcurrent_ans += B[i]とした方が可読性が上がる
# 回答の0か正の値かを判定する場合は、max()関数を使用した方が意図が伝わり、可読性が上がる

N, M = list(map(int, input().split()))
B = [i for i in list(map(int, input().split()))]
W = [i for i in list(map(int, input().split()))]
B = sorted(B, reverse=True)
W = sorted(W, reverse=True)
current_ans = 0
ans = float('-inf')

for i in range(N):
    if i < M:
        current_ans += B[i]
        if current_ans < current_ans + W[i]:
            current_ans += W[i]
        ans = max(current_ans, ans)
    else:
        current_ans = current_ans + B[i]
        ans = max(current_ans, ans)

print(max(ans, 0))
