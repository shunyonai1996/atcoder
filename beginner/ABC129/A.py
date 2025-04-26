import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

P, Q, R = list(map(int, input().split()))
print(min(P+Q, Q+R, P+R))