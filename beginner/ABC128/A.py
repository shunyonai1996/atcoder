import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

A, P = list(map(int, input().split()))
print((A * 3 + P)//2)