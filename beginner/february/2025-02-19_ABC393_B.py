import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue

# 条件分岐
# 三つの文字が違う文字列である場合
# かつ、文字列内が等間隔であること j−i=k−j

S = str(input())
list = list(S)

for i in range(0, len(S)-1):
    list[i]==list[i+1]
    print(list[i])

# 解答例
# s = input()
# n = len(s)
# ans = 0

# for i in range(n):
#   for j in range(i + 1, n):
#     for k in range(j + 1, n):
#       if j - i == k - j and s[i] == 'A' and s[j] == 'B' and s[k] == 'C':
#         ans += 1

# print(ans)