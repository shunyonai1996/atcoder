import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
A = [i for i in list(map(int, input().split()))]
ans = False

for i in range(2, N):
    if A[i-2] == A[i-1] ==A[i]:
        ans = True
if ans:
    print('Yes')
else:
    print('No')
