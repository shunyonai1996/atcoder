import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))
flg = True

for i in range(1, N):
    if A[i-1] >= A[i]:
        print('No')
        flg = False
        break

if flg:
    print('Yes')