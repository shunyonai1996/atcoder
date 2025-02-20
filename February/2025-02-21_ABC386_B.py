import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 入力の数値を1文字ずつ分割
# 0の場合のみ、次の数値が0か判定
# 0が連続する場合、フラグを使う？
# 要素数を返すため、解答を変数でカウントアップ

S = input()
answer = 0
is_zero = False

for i in range(0, len(S)):
    if S[i] != '0':
        answer += 1
    elif is_zero == False:
        if i < len(S)-1 and S[i+1] == '0':
            answer += 1
            is_zero = True
        else:
            answer += 1
    else:
        is_zero = False

print(answer)