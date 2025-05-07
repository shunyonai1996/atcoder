import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

maps = [i for i in range(1, N+1)]
Pi = itertools.permutations(maps, N)
Qi = itertools.permutations(maps, N)

p_cnt = 1
for i in Pi:
    if i == P:
        break
    p_cnt += 1

q_cnt = 1
for i in Qi:
    if i == Q:
        break
    q_cnt += 1

print(abs(p_cnt - q_cnt))