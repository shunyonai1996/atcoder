import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, M = map(int, input().split())
S = list(map(int, input().split()))
ans = []

for i in range(1, N+1):
    if i not in S:
        ans.append(i)

if len(ans) > 0:
    print(len(ans))
    print(*ans)
else:
    print(0)