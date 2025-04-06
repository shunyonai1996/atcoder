import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, M = list(map(int, input().split()))

X = 1
for i in range(M):
    X += N ** (i+1)
if X <= 10 ** 9:
    print(X)
else:
    print('inf')