N, M = map(int, input().split())
H = list(map(int, input().split()))

bad = []
for i in range(M):
    a, b = map(int, input().split())
    if H[a-1] < H[b-1]:
        bad.append(a)
    elif H[a-1] == H[b-1]:
        bad.append(a)
        bad.append(b)
    else:
        bad.append(b)

print(N - len(set(bad)))