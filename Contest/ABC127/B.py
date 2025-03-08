import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

r, D, x = list(map(int, input().split()))
weight = x

for i in range(10):
    weight = r * weight - D
    print(weight)