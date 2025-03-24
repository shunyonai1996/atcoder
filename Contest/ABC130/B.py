import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, X = list(map(int, input().split()))

L = [int(l) for l in list(input().split())]

print(N, X, L)