import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

L, R = map(int, input().split())
if 2019 <= R - L:
    print('0')
else:
    min_val = float('inf')
    for i in range(L, R):
        for j in range(L+1, R+1):
            min_val = min(min_val, (i * j) % 2019)
            if min_val == 0:
                break
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

# AIの別解
L, R = map(int, input().split())

# 範囲が2019以上あるなら、必ず mod 2019 で 0 が作れる
if R - L >= 2019:
    print(0)
else:
    min_val = float('inf')
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            min_val = min(min_val, (i * j) % 2019)
            if min_val == 0:
                print(0)
                exit()
    print(min_val)