import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

A, B = list(map(int, input().split()))

if (A + B) % 2 == 0:
    print((A + B) // 2)
else:
    print('IMPOSSIBLE')
