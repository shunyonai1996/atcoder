import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import sys
input = sys.stdin.readline

N = int(input())
S = list(input().strip())
ans = 0
pre_color = None

for i in range(N):
    if S[i] == pre_color:
        continue
    else:
        ans += 1
        pre_color = S[i]

print(ans)