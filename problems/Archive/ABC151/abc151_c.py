import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
ac_cnt = 0
wa_cnt = 0
acs = [0] * (N+1)
was = [0] * (N+1)

for i in range(M):
    q, r = map(str, input().split())
    q = int(q)
    if acs[q] == 0 and r == 'AC':
        ac_cnt += 1
        acs[q] = 1
        wa_cnt += was[q]
        if ac_cnt == N:
            break
    elif acs[q] == 0 and r == 'WA':
        was[q] += 1
print(ac_cnt, wa_cnt)