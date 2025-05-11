# N, M = map(int, input().split())
# A = list(map(int, input().split()))

# ans = 0
# for i in range(N):
#     ok = True
#     for j in range(1, M+1):
#         if j in A:
#             continue
#         else:
#             ok = False
#     if ok:
#         del A[-1]
#         ans += 1
#     else:
#         break
# print(ans)

# # 後日再回答
# N, M = map(int, input().split())
# A = [x - 1 for x in map(int, input().split())]
# ans = 0

# while True:
#     exist = [False] * M
#     for i in A:
#         exist[i] = True
#     if not all(exist):
#         break
#     A.pop()
#     ans += 1
# print(ans)

# AIの別解
n, m = map(int, input().split())
a = [x-1 for x in list(map(int, input().split()))]
ans = 0

current = set(a)
while all(i in current for i in range(m)):
    a.pop()
    current = set(a)
    ans += 1

print(ans)