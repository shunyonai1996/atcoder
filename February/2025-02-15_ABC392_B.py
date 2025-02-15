import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# l = [list(map(int, input().split())) for i in range(2)]
# n = l[0][0]
# a = l[1]
# answer = []

# for i in range(1,n+1):
#     if i not in a:
#         answer.append(i)
#     i+=1 # rangeで制御しているため不要

# if len(answer) > 0:
#     print(len(answer))
#     print(*answer)
# else:
#     print(0)

# AIの回答1
# N, M = map(int, input().split())
# A = set(map(int, input().split()))
# answer = sorted(set(range(1, N+1)) - A)
# print(A)
# print(answer)
# if answer:
#     print(len(answer))
#     print(*answer)
# else:
#     print(0)

# AIの回答2
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# answer = [i for i in range(1, N+1) if i not in A]
# if answer:
#     print(len(answer))
#     print(*answer)
# else:
#     print(0)

# AIの回答3
N, M = map(int, input().split())
A = list(map(int, input().split()))
used = [False] * (N+1)
for a in A:
    used[a] = True
answer = [i for i in range(1, N+1) if not used[i]]
if answer:
    print(len(answer))
    print(*answer)
else:
    print(0)