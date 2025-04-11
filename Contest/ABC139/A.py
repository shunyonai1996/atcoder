import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

S = list(str(input()))
T = list(str(input()))
ans = 0

for i in range(3):
    if S[i] == T[i]:
        ans += 1
print(ans)