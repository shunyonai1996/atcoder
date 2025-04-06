import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import math

a = 400 / int(input())
if a % 1 == 0:
    print(math.floor(a))
else:
    print('-1')