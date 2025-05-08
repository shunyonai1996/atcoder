H, K = map(int, input().split())
H = sorted(map(int, input().split()), reverse=True)

if len(H) <= K:
    print('0')
else:
    print(sum(H[K:]))