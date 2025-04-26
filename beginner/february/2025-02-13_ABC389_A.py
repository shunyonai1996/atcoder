import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

a = list(input())
num1, num2 = int(a[0]), int(a[2])
print(num1*num2)

# AIの回答1
# strでinputで受け取るため、list形式に変換が必要な認識だった
# strの[i]番目を取り出すことが可能、つまりlistへの変換不要

# S = input()
# num1, num2 = int(S[0]), int(S[2])
# print(num1 * num2)

# AIの回答2
# S = input()
# nums = S.split('x')
# print(int(nums[0]) * int(nums[1]))