import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = sorted(list(map(int, input().split())))
T = [0]+[0] * 13

for i in N:
    T[i-1] += 1

x = False
y = False

for i in sorted(T):
    if 2 <= i <= 5 and x == False:
        x = True
    elif 3 <= i <= 5:
        y = True

if x and y:
    print('Yes')
else:
    print('No')