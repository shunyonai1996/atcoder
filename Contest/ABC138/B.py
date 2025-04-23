import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# 逆数 1 / (1 / A1 + 1 / A2...)

N = int(input())
A = map(int, input().split())

denominator = 0
for num in A:
    denominator += 1 / num
print(1 / denominator)