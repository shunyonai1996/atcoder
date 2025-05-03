import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))

# AIのフィードバック
# Nが2のケースの特別扱いNG
# 浮動小数点の助産による誤差が起きる可能性がある

if N == 2:
    print("Yes")
else:
    x = A[1] / A[0]
    check_list = [A[i-1] * x for i in range(1,N)]
    check_list.insert(0,A[0])
    if check_list == A:
        print('Yes')
    else:
        print('No')

# AIの別解1
# is_geometric = True
# if N > 1:
#     # 隣接する要素の比が一定かどうかを整数の乗算で確認
#     for i in range(N-2):
#         if A[i] * A[i+2] != A[i+1] * A[i+1]:
#             is_geometric = False
#             break
# print("Yes" if is_geometric else "No")

# AIの別解2
# is_geometric = True
# if N > 1:
#     # 最初の比を基準とする
#     first_ratio = A[1] / A[0]
#     # 隣り合う項の比が全て同じかチェック
#     for i in range(1, N-1):
#         current_ratio = A[i+1] / A[i]
#         # 誤差を考慮した比較
#         if abs(current_ratio - first_ratio) > 1e-10:
#             is_geometric = False
#             break
# print("Yes" if is_geometric else "No")