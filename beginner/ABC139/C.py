import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as f:
    INPUT=f.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
hop_counter = 0
hops = 0

for i in range(N-1):
    if H[i] >= H[i+1]:
        hop_counter += 1
    else:
        hops=max(hops, hop_counter)
        hop_counter = 0

print(max(hops, hop_counter))