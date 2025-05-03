import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))

ans = 0
isEven = True
while isEven == True:
    for i in range(N):
        if A[i] % 2 != 0:
            isEven = False
        A[i] = A[i] / 2
    if isEven:
        ans += 1
print(ans)