import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# スタックで考える
# =====ループ内====
# 入力を１文字ずつスタックに入れる
# variable_listとstack_listが一致する場合、match_listに追加する
# stack_listが7文字を超えたらループ終了
# =====ループ内====
# stack_listが空なら'YES',ないなら'NO'

S = input()
variable_list = ['maerd', 'esare', 'remaerd', 'resare']
stack_list = []

for char in reversed(S):
    stack_list.append(char)
    if stack_list in variable_list:
        stack_list.clear()

    if 7 < len(stack_list):
        break
print('NO') if stack_list else print('YES')



# AIによる別解
S = input()
n = len(S)
dp = [False] * (n + 1)
dp[0] = True  # 空文字列は常に作成可能

words = ["dream", "dreamer", "erase", "eraser"]

for i in range(n):
    if not dp[i]:
        continue

    for word in words:
        if S[i:i+len(word)] == word:
            dp[i+len(word)] = True

print("YES" if dp[n] else "NO")