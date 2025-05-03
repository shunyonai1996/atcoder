import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 文字列に対して'WA'が含まれるかチェック
# 含まれる場合、その箇所を'AC'に置換
# 置換した後の文字列に対して'WA'が含まれるかチェック
# 含まれる場合、その箇所を'AC'に置換...

# AIによるリファクタ
# 出力をfor->joinにするだけでO(nの2の累乗)からO(n)に計算量が削減できる
# `i == 0`のケースはほぼないため、elseと入れ替え

S = list(input())
i = 0

while i < len(S) - 1:
    if S[i] == 'W' and S[i+1] == 'A':
        S[i], S[i+1] = 'A', 'C'
        if i > 0:
            i -= 1
        else:
            i += 1
    else:
        i += 1

print("".join(S))