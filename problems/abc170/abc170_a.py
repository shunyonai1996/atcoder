import io,sys
with open("../../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

a = list(map(int, input().split()))

[print(i+1) for i in range(5) if a[i] == 0]