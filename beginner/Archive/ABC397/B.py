import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# S = list(map(str, input()))
# ans = 0

# for index in range(1, 200):
#     if index % 2 == 0:
#         if S[index - 1] != 'o':
#             S.insert(index - 1, 'o')
#             ans += 1
#     else:
#         if S[index - 1] != 'i':
#             S.insert(index - 1, 'i')
#             ans += 1
#     if index == len(S):
#         if len(S) % 2 != 0: ans += 1
#         break

# print(ans)

# 解説
# 初期値をiとし、iとoを反転させ、Sと一致するかどうか判定

S = list(input())
value = 'i'
ans = 0

for i in S:
    if i == value:
        value = 'o' if value == 'i' else 'i'
    else:
        ans += 1

if value == 'o': ans += 1
print(ans)
