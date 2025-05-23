import io,sys
with open("../../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

X, Y = map(int, input().split())

for t in range(0, X * 2 + 1, 2):
    for k in range(0, X * 4 + 1, 4):
        if t + k == Y and X * 2 <= t + k and t + k <= X * 4:
            print('Yes')
            exit()

print('No')
