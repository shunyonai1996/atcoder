import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
H = list(map(int, input().split()))
cur_v = 0
for i in range(N):
    if H[i] < cur_v - 1:
        print('No')
        exit()
    if cur_v < H[i]:
        cur_v = H[i]
print('Yes')