import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

H, W = list(map(int ,input().split()))
A = [list(input()) for a in range(H)]
B = [list(input()) for a in range(H)]
match = False

for s in range(H):
    for t in range(W):
        if A == B:
            match = True
            break
        A = [list[1:] + [list[0]] for list in A]
    if match: break
    A = A[1:] + [A[0]]
print('Yes') if match else print('No')