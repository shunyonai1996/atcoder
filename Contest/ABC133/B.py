import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, D = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]

# N回のループでN
# 
print(X)

for i in range(N-1):
    for j in range(D-1):
        print(X[i][j] - [j+1])
        print(X[i+1][j] - X[i+1][j+1])