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

# AIによる別解
import sys
N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

ans = 1 if N >= 1 else 0
for i in range(1, N):
    if S[i] != S[i-1]:
        ans += 1
print(ans)