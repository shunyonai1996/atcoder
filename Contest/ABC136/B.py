import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = str(input())
ans = 0

for i in range(0, len(N)):
    if i % 2 == 0 and i == len(N)-1:
        ans += int(N)-10**i+1
    elif i % 2 == 0:
        ans += 9 * 10**i
print(ans)