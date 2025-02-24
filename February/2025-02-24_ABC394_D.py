import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# `()``[]``<>`いずれかの連続した文字列がある場合、対象の文字列を削除
# 検知した時点で文字列を削除し、再度最初からループ
# 連続した文字列が検知できない場合はNoを返す
# 空配列ならYesを返す

S = input()

while 0 < len(S):
    if '()' in S:
        S = S.replace('()', '')
    elif '[]' in S:
        S = S.replace('[]', '')
    elif '<>' in S:
        S = S.replace('<>', '')
    else:
        break

print('Yes') if len(S) == 0 else print('No')