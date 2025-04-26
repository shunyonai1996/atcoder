import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# `()``[]``<>`いずれかの連続した文字列がある場合、対象の文字列を削除
# 検知した時点で文字列を削除し、再度最初からループ
# 連続した文字列が検知できない場合はNoを返す
# 空配列ならYesを返す

# AIによるソースレビュー
# O(N^2)のため、実行時間を超過する
# replaceでフルスキャンと文字列の置換を

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

# AIの回答
# O(N)を実現している
def is_colorful_bracket_string(S: str) -> str:
    stack = []
    matching = {')': '(', ']': '[', '>': '<'}

    for char in S:
        if char in "([<":  # 開き括弧はスタックに追加
            stack.append(char)
        elif char in ")]>":  # 閉じ括弧が出た場合
            if not stack or stack[-1] != matching[char]:  
                return "No"  # 期待する開き括弧でなければNG
            stack.pop()  # 対応する括弧を削除

    return "Yes" if not stack else "No"

S = input()
print(is_colorful_bracket_string(S))