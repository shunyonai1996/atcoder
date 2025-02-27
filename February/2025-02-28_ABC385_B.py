import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# XYの初期値を変数で保持
# 地図をマッピング
# 最終行の入力によって、XYを移動
H, W, X, Y = list(map(int, input().split()))
santa = [X, Y]
S = []
present = 0

for i in range(H):
    S.append(list(input()))

T = list(input())
for value in T:
    if S[santa[0]][santa[1]] == '@':
        S[santa[0]][santa[1]] = 'v'
        present += 1
    if value == 'U':
        print(S[santa[0]][santa[1]])
        santa = [santa[0]-1,santa[1]]
        if S[santa[0]-1][santa[1]] == '#':
            continue
    elif value == 'D':
        if S[santa[0]+1][santa[1]] == '#':
            continue
        santa = [santa[0]+1,santa[1]]
    elif value == 'L':
        if S[santa[0]][santa[1]-1] == '#':
            continue
        santa = [santa[0],santa[1]-1]
    elif value == 'R':
        if S[santa[0]][santa[1]+1] == '#':
            continue
        santa = [santa[0],santa[1]+1]
    print(present)

print(f'{santa[0]+1} {santa[1]+1} {present}')