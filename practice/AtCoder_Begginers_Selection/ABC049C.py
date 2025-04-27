import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# スタックで考える
# 空のリストを作る
# Sをループで回す
# =====ループ内====
# stack_listに値を追加
# variable_listと突合
# 一致する場合、文字数を記録
# 上記に一致する場合、n文字進める
# =====ループ内====

S = input()
variable_list = ['maerd', 'esare', 'remaerd', 'resare']
stack_list = []

for char in reversed(S):
    stack_list.append(char)
    value = [v for v in variable_list if ''.join(stack_list) == v]
    if value:
        stack_list.clear()
    if 7 < len(stack_list):
        break
print('NO') if stack_list else print('YES')