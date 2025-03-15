import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

H, W = list(map(int ,input().split()))
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]
match = False

for s in range(H):
    for t in range(W):
        if A == B:
            match = True
        A = [row[1:] + [row[0]] for row in A]
    if match: break
    A = A[1:] + [A[0]]
print('Yes') if match else print('No')


# AIによる別解
from collections import deque

H, W = map(int, input().split())
# ポイントは縦方向シフトに対応するため、リストの中のリストをdeque()形式にすること
A = [deque(input()) for _ in range(H)]
print(A)
B = [deque(input()) for _ in range(H)]
print(B)

match = False

for s in range(H):
    for t in range(W):
        if A == B:
            match = True
            break
        for row in A:
            row.rotate(-1)  # 横方向のシフト
    if match:
        break
    A.append(A.pop(0))  # 縦方向のシフト

print("Yes" if match else "No")
