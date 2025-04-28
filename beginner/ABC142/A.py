import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())

if N == 1:
    print("{:.10f}".format(1))
elif N % 2 == 0:
    print("{:.10f}".format(0.5))
else:
    ans = ((N + 1) / 2) / N
    print("{:.10f}".format(ans))
