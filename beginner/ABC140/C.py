import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as f:
    INPUT=f.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))
A = 0

if 2 < N:
    for i in range(1, N-1):
        A += min(B[i-1], B[i])
    print(B[0]+A+B[-1])
else:
    print(B[0]*2)