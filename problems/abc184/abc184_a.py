import io,sys
with open("input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

print(a * d - b * c)