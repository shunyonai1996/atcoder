N = int(input())
testimonies = [[] for _ in range(N)]
max_honest = 0

for i in range(N):
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        testimonies[i].append((x-1, y))

for bit in range(2**N):
    ok = True
    for i in range(N):
        if not (bit >> i) & 1:
            continue
        for x, y in testimonies[i]:
            if ((bit >> x) & 1) != y:
                ok = False
                break
        if not ok:
            break
    if ok:
        count = bin(bit).count('1')
        max_honest = max(count, max_honest)

print(max_honest)