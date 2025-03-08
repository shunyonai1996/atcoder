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
print(B,W)
before_ans = 0
ans = 0

for i in range(len(W)):
    if before_ans + B[i] + W[i] > before_ans + B[i]:
        ans = before_ans + B[i] + W[i]
        before_ans = ans
    elif before_ans > before_ans + B[i]:
        print(ans)

if 0 < ans:
    print(ans)
else:
    print(0)