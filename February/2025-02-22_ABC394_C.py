import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 文字列に対して'WA'が含まれるかチェック
# 含まれる場合、その箇所を'AC'に置換
# 置換した後の文字列に対して'WA'が含まれるかチェック
# 含まれる場合、その箇所を'AC'に置換...

S = list(input())
i = 0
answer = ''

while i < len(S)-1:
    if S[i] == 'W' and S[i+1] == 'A':
        S[i],S[i+1] = 'A','C'
        if i == 0:
            i += 1
        else:
            i -= 1
    else:
        i += 1

for i in range(len(S)):
    answer += S[i]

print(answer)