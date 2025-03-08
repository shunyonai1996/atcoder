import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

Q = int(input())
C = [list(map(int, input().split())) for _ in range(Q)]
cards = [0]

for i in range(Q):
    if C[i][0] == 2:
        if len(cards) == 1:
            print(cards[-1])
        else:
            print(cards[-1])
            cards.pop(-1)
    else:
        cards.append(C[i][1])