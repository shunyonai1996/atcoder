import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# ループ回す
# Aだったら、等間隔の文字列をチェック
# rangeオーバーにならないために

S = list(input())
ans = 0

for i, v in enumerate(S):
    print(f'{i}番目{v}')
    if v == 'A':
        for index in range(1, len(S)):
            print(3*index,len(S))
            if len(S) >= 3 * index:
                if S[index] == 'B' and S[2*index] == 'C':
                    ans += 1
print(ans)