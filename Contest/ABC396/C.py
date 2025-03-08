import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, M = list(map(int, input().split()))
B = [i for i in list(map(int, input().split()))]
W = [i for i in list(map(int, input().split()))]
B = sorted(B, reverse=True)
W = sorted(W, reverse=True)
current_ans = 0
ans = float('-inf')

for i in range(N):
    if i < M:
        current_ans = current_ans + B[i]
        if current_ans < current_ans + W[i]:
            current_ans += W[i]
        ans = max(current_ans, ans)
    else:
        current_ans = current_ans + B[i]
        ans = max(current_ans, ans)

if 0 < ans:
    print(ans)
else:
    print(0)