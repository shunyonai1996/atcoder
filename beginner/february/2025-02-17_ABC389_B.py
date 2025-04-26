import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue整理
# 回答を逆算する
# 1からnまでループで全て掛けていき、inputとi番目のループが一致した時点でprint

# AIによるコードレビュー
# 20!が2.4*10の18乗を越えるため、それ以上は不要
# 変数名を適当なものに修正

X = int(input())
result = 1
for i in range(1,X+1):
    result*=i
    if X == result:
        print(i)
        break

# AIによる別解1
# X = int(input())

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# left, right = 1, 20
# while left <= right:
#     mid = (left + right) // 2
#     fact = factorial(mid)
#     if fact == X:
#         print(mid)
#         break
#     elif fact < X:
#         left = mid + 1
#     else:
#         right = mid - 1

# AIによる別解2
# X = int(input())
# facts = [1]  # 0!
# for i in range(1, 21):
#     facts.append(facts[-1] * i)

# for i, f in enumerate(facts):
#     if f == X:
#         print(i)
#         break