import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import math
N, D = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N-1):
    for j in range(i, N-1):
        calc_list = [(x - y) ** 2 for x, y in zip(X[i], X[j+1])]
        sqrt_list = math.sqrt(sum(calc_list))
        if sqrt_list % 1 == 0:
            ans += 1
print(ans)
