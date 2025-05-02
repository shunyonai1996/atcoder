import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import sys
input = sys.stdin.readline

N, K, Q = list(map(int, input().split()))
N = [K] * N

for i in range(1, Q+1):
    input_val = int(input())
    if K <= i and 0 < i-N[input_val-1]:
        continue
    else:
        N[input_val-1] += 1

for i in map(int, N):
    if 0 < i-Q:
        print('Yes') 
    else:
        print('No')