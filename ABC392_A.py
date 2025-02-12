import io,sys
with open("input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

a = list(map(int, input().split()))

a0, a1, a2 = a

if a0 * a1 == a2:
    print('Yes')
elif a0 * a2 == a1:
    print('Yes')
elif a1 * a0 == a2:
    print('Yes')
elif a1 * a2 == a0:
    print('Yes')
elif a2 * a0 == a1:
    print('Yes')
elif a2 * a1 == a0:
    print('Yes')
else:
    print('No')


# AIの回答例
# 例1

# x, y, z = sorted(a)
# print('Yes' if x * y == z else 'No')


# 例2

# def check_multiplication(nums):
#     return any(nums[i] * nums[j] == nums[k]
#               for i in range(3)
#               for j in range(i+1, 3)
#               for k in range(3)
#               if k != i and k != j)
# print('Yes' if check_multiplication(a) else 'No')