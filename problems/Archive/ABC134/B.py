import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, D = list(map(int, input().split()))
if N <= D:
    print('1')
else:
    ans = 0
    for i in range(0, N, D*2+1):
        if i + (D * 2) < N:
            ans += 1
        else:
            ans += 1
    print(ans)
