import io,sys
with open("input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------


a, b, c, d =map(int, input().split())

print(max(a * c, a * d, b * c, b * d))