import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import sys
input = sys.stdin.readline

N = int(input())
s = [''.join(sorted(input().strip())) for _ in range(N)]
ans=0
d = {}

for char in s:
    if char not in d:
        d[char] = 0
    d[char] += 1

for v in d.values():
    ans += v * (v - 1) / 2

print(f"{ans:.0f}") 