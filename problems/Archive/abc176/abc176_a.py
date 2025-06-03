import io,sys
with open("input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import math
N, X, T = map(int, input().split())

a = math.ceil(N / X)
print(a * T)