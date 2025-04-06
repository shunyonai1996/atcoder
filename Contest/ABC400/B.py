import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, M = map(int, input().split())
X = sum(N ** i for i in range(M+1))
print(X) if X <= 10 ** 9 else print('inf')