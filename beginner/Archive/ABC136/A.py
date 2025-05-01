import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

A, B, C = list(map(int, input().split()))

if (C - (A - B)) > 0:
    print(C - (A - B))
else:
    print(0)
