import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
P = list(map(int, input().split()))
diff_cnt = 0

for i in range(1, N+1):
    if i != P[i-1]:
        diff_cnt += 1
print('NO') if 3 <= diff_cnt else print('YES')