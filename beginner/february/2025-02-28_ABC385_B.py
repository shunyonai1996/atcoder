import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
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


# 解説記事の解答
H,W,X,Y = map(int,input().split())
S = [list(input()) for _ in range(H)]
T = input()

# リストで扱うため-1
X-=1
Y-=1
ans=0
for c in T:
  # 文字列チェック、かつ'#'ではない
  if c=='U' and S[X-1][Y]!='#': X-=1
  if c=='D' and S[X+1][Y]!='#': X+=1
  if c=='L' and S[X][Y-1]!='#': Y-=1
  if c=='R' and S[X][Y+1]!='#': Y+=1
  # '@'なら加算し、無効化する
  if S[X][Y]=='@':
    ans+=1
    S[X][Y]='.'

# リストで扱ったXYを+1
print(X+1,Y+1,ans)