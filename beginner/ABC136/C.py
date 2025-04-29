import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import sys
input = sys.stdin.readline

N = int(input())
ans = 0
s = [sorted(str(input()).strip()) for i in range(N)]

for char in s:
    cnt = s.count(char)
    if 1 < cnt:
        ans += (cnt-1)/2
print(f"{ans:.0f}") 