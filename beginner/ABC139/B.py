import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

A, B = map(int, input().split())

hole = A
ans = 1
while hole < B:
    hole += A-1
    ans += 1

print('0') if B == 1 else print(ans)
