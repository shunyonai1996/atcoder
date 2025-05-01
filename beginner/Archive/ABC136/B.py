import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = str(input())
ans = 0

for i in range(0, len(N)):
    if i % 2 == 0 and i == len(N)-1:
        ans += int(N)-10**i+1
    elif i % 2 == 0:
        ans += 9 * 10**i
print(ans)

# AIによる別解
N = int(input())
count = 0

for num in range(1, N + 1):
    # 数字を文字列に変換して桁数を調べる
    if len(str(num)) % 2 == 1:
        count += 1

print(count)

N = int(input())
digit_count = len(str(N))
result = 0

# 1桁、3桁、5桁...の数の合計を計算
for digits in range(1, digit_count + 1, 2):
    if digits < digit_count:
        # 完全な桁数（例: 1桁なら9個、3桁なら900個）
        result += 9 * 10**(digits-1)
    else:
        # 最後の桁数（例: Nが1234なら、1000から1234までの数）
        result += N - 10**(digits-1) + 1

print(result)
