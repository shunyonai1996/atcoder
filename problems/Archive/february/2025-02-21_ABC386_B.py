import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 入力の数値を1文字ずつ分割
# 0の場合のみ、次の数値が0か判定
# 0が連続する場合、フラグを使う？
# 要素数を返すため、解答を変数でカウントアップ

# AIによるコードレビュー
# if文内のBool型の記述は`if Bool`や`if not Bool`とすべき
# rangeは引数一つなら、引数で指定した回数を0から実行する

S = input()
answer = 0
is_zero = False

for i in range(len(S)):
    if S[i] != '0':
        answer += 1
    elif not is_zero:
        if i < len(S)-1 and S[i+1] == '0':
            answer += 1
            is_zero = True
        else:
            answer += 1
    else:
        is_zero = False

print(answer)


# AIによる別解1
# whileを使用して、インデックスの増加幅をロジック側で制御可能
# よって、0が連続するかどうか判定するフラグが不要となる
# for文はイテラブルから要素を1つずつ取り出すイテレータに基づいてループを実行するため、インデックスを動的に増加できない
S = input()
answer = 0
i = 0
length = len(S)

while i < length:
    if S[i] != '0':
        answer += 1
        i += 1
    else:
        if i + 1 < length and S[i+1] == '0':
            answer += 1
            i += 2
        else:
            answer += 1
            i += 1

print(answer)