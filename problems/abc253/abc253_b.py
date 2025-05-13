H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
pieces = []

for h in range(H):
    for w in range(W):
        if S[h][w] == 'o':
            pieces.append([h, w])
            if len(pieces) == 2:
                break

print(abs(pieces[0][0] - pieces[1][0]) + abs(pieces[0][1] - pieces[1][1]))
