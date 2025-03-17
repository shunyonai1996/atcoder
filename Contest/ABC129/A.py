import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

P, Q, R = list(map(int, input().split()))
print(min(P+Q, Q+R, P+R))