import io,sys
with open("input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))

max_count = 0
ans = 0
for i in range(2, 1001):
    count = 0
    for j in range(N):
        if A[j] % i == 0:
            count += 1
    if max_count <= count:
        max_count = count
        ans = i

print(ans)