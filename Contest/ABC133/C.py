import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

L, R = map(int, input().split())
min_val = float('inf')

if 2019 < R - L:
    loop_cnt = L + 2019
else:
    loop_cnt = R

for i in range(L, loop_cnt):
    for j in range(L, loop_cnt):
        min_val = min(min_val, (i * (j + 1)) % 2019)
        if min_val == 0:
            break
print(min_val)


# 解説記事をpython変換
L = 0
R = 0
inf = 10**9

def chmin(a, b):
    return b if b < a else a

def solve():
    ans = inf
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            ans = chmin(ans, (i * j) % 2019)
            if ans == 0:
                return 0
    return ans

def main():
    global L, R
    L, R = map(int, input().split())
    print(solve())