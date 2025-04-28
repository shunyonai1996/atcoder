import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# 全体方針
    # 街N[i] -> A[i]体の怪獣がいる -> 勇者N[i]がB[i]体の怪獣を消すmin(A[i], (B[i]))
    # 街N[i+1] -> A[i+1]体の怪獣がいる -> 
    # 勇者N[i+1]がmin(A[i], (B[i]+prestuck))体の怪獣を消す
    # (B[i+1]+prestuck)-
    # max(0, min(B[i+1], (B[i+1]+prestuck) - A[i+1]))
    # ...ループ

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
pre_stuck = 0

for i in range(N):

    ans += min(A[i], B[i]+pre_stuck)
    pre_stuck = max(0, min(B[i], (B[i]+pre_stuck)-A[i]))

if 0 < pre_stuck:
    ans += min(A[N], pre_stuck)

print(ans)