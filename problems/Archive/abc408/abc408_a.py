N, S = map(int, input().split())
T = list(map(int, input().split()))

if S < T[0]:
    print('No')
    exit()

for i in range(N-1):
    if S < T[i+1] - T[i]:
        print('No')
        exit()

print('Yes')