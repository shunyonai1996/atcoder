import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

A = list(map(int, input().split()))

print('bust') if 22 <= sum(A) else print('win')