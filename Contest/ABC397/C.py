import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    if ans < len(set(A[:i])) + len(set(A[i:])):
        ans = len(set(A[:i])) + len(set(A[i:]))
print(ans)