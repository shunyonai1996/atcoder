import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

A, B, C, X = [int(input()) for _ in range(4)]
ans = 0

for a in range(0, A+1):
    if 500 * a <= X:

        for b in range(0, B+1):
            if 100 * b <= X:

                for c in range(0, C+1):
                    if 50 * c <= X:
                        if (500 * a) + (100 * b) + (50 * c) == X:
                            ans += 1
print(ans)