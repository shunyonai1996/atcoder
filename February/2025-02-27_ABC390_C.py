import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 連続したリストから四角の判定をする方法検討
# `.`によって四角を作れない事象検証

# 1行内での検証
# `#`の間に`.`があったらNo
# `#`の間が`?`か`#`ならYes
# 最初に`#`が現れた時に塗りつぶす必要のあるインデックスをリストで保存

# 前の行から正方形を作れるか

# ×NGの行があった場合、処理を終了

H,W = list(map(int, input().split()))

check_list = [0] * W
flg = False
cnt = 0

for i in range(H):
    S = list(*input().split())
    if flg == False and '#' in S:
        flg = True
        for i, name in enumerate(S):
            if name == '#' or name == '?':
                check_list[i] = 1
    elif flg:
        for i, value in enumerate(check_list):
            if check_list[value] == 1 and (S[i] == '#' or S[i] == '?'):
                continue
            elif check_list[value] == 0 and (S[i] == '#'):
                print('No')
                break