import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 問題の条件を満たしていること

H, W = list(map(int, input().split()))
N = min(H, W)
print(H, W, N)

list = [list(str(input())) for _ in range(H)]
print(list)