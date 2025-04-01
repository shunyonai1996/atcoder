import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, D = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(D):
        print(i, j)