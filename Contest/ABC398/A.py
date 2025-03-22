import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
ans = ['-'] * N

if N % 2 == 0:
    ans[int(N / 2) - 1] = '='
    ans[int(N / 2)] = '='
else:
    ans[int((N-1) / 2)] = '='

print(''.join(ans))