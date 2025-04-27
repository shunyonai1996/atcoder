import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/beginner/ABC403/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

pn, pm, pq = list(map(int, input().split()))
mapping = [[0] * (pm + 1) for _ in range(pn + 1)]
can_view_all = [False] * (pn+1)

for _ in range(pq):
    t, *q = list(map(int, input().split()))
    if t == 2:
        can_view_all[q[0]] = True
    else:
        if t == 3:
            if can_view_all[q[0]] == True or mapping[q[0]][q[1]] == 1:
                print('Yes')
            else:
                print('No')
        else:
            mapping[q[0]][q[1]] = 1