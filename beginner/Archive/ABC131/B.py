import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, L = list(map(int, input().split()))
apple_score = [L + i - 1 for i in range(1, N + 1)]

if 0 in apple_score:
    print(sum(apple_score))
elif L < 0:
    abs_apple_score = sorted([abs(L + i - 1) for i in range(1, N + 1)], reverse=True)
    print(sum(apple_score) - min(abs_apple_score) * -1)
else:
    abs_apple_score = sorted([abs(L + i - 1) for i in range(1, N + 1)], reverse=True)
    print(sum(apple_score) - min(abs_apple_score))
