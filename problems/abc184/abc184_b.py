import io,sys
with open("input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------
N, X = map(int, input().split())
S = input()

for i in range(N):
    if S[i] == 'o':
        X += 1
    else:
        if X > 0:
            X -= 1

print(X)