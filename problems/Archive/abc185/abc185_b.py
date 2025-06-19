N, M, T = map(int, input().split())

power = N
pass_time = 0

for i in range(M):
    a, b = map(int, input().split())
    power -= a - pass_time
    if power <= 0:
        print('No')
        exit()
    power =  min(N, power + b - a)
    pass_time = b

if pass_time != T:
    power -= (T - pass_time)
    if power <= 0:
        print('No')
        exit()

print('Yes')