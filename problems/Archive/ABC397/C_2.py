import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
A = list (map(int, input().split()))
prefix = [0] * N
suffix = [0] * N
ans = 0
count = 0
seen = set()

for i in range(N):
    if A[i] not in seen:
        seen.add(A[i])
        count += 1
    prefix[i] = count

# suffix = list(reversed(prefix))でも良いが、累積和の逆転の考え方を使用するため、以下の記載をしている
seen = set()
count = 0
for i in range(N-1, -1, -1):
    if A[i] not in seen:
        seen.add(A[i])
        count += 1
    suffix[i] = count

for i in range(N-1):
    ans = max(ans, prefix[i] + suffix[i+1])
print(ans)
