# import copy

# A = [1, 2, 3]
# B = copy.copy(A)  # 浅いコピー

# print(f"A: {A}")
# print(f"B: {B}")

# A[0] = 100
# print(f"A: {A}")
# print(f"B: {B}")

# B[1] = 200
import copy

A = [[1,2,3], [4,5,6], [7,8,9]]
B = copy.copy(A)  # 浅いコピー
print(f"A: {A}")
print(f"B: {B}")

A[0] = [100, 101]
print(f"A: {A}")
print(f"B: {B}")

# 新規作成したオブジェクトのため、値の更新が
A[1][0] = 200
print(f"A: {A}")
print(f"B: {B}")