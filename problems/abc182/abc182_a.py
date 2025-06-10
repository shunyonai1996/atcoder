import io,sys
with open("input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

A, B = map(int, input().split())

if 0 <= (2 * A + 100) - B:
    print((2 * A + 100) - B)
else:
    print(0)