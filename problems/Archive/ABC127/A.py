import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

A, B = list(map(int, input().split()))

if 13 <= A:
    print(B)
elif 6 <= A <= 12:
    print(B//2)
else:
    print(0)
