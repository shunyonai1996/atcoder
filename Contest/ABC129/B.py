import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
W = list(map(int, input().split()))

ans_list = []
for i in range(1, N):
    first = W[:i]
    second = W[i:]
    total = abs(sum(first) - sum(second))
    ans_list.append(total)

print(min(ans_list))