import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, M = list(map(int, input().split()))
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(M)]

for a in range(N - M + 1):
    for b in range(N - M + 1):
        ok = True
        for i in range(M):
            for j in range(M):
                if S[a + i][b + j] != T[i][j]:
                    ok = False
        if ok:
            print(a + 1, b + 1)