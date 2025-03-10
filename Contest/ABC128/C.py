import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------


N, M = list(map(int, input().split()))
switches = ((0, 0),) + ((0, 1),) * N
print(switches)
ks = [[]] + [list(map(int, input().split())) for i in range(N)]
P = list(map(int, input().split()))

for k in range(1, N+1):
    print(ks[k])
    for s in range(1, ks[k][0]+1):
        print(switches[ks[k][s]])