import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
S = list(str(input()))
T = list(str(input()))

ans = 0
for i in range(N):
    if S[i] != T[i]:
        ans += 1

print(ans)
