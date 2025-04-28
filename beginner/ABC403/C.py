import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as f:
    INPUT=f.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
can_view = [set() for _ in range(N + 1)]
can_view_all = [False] * (N + 1)

for _ in range(Q):
    t, *queue = map(int, input().split())
    x = queue[0]
    if t == 1:
        can_view[x].add(queue[1])
    elif t == 2:
        can_view_all[x] = True
    else:
        if can_view_all[x] or queue[1] in can_view[x]:
            print('Yes')
        else:
            print('No')