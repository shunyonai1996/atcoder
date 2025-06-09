import io,sys
with open("input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
cnt = 0


for i in range(N):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        cnt += 1
    else:
        if cnt == 3:
            print('Yes')
            exit()
        elif 0 < cnt:
            cnt = 0

if cnt >= 3:
    print('Yes')
else:
    print('No')