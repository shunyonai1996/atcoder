import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# Xの座標を起点に前後K個の座標を順番に出力する
# K, X = list(map(int, input().split()))
# min_val, max_val = X-K+1,X+K-1

# [print(i) for i in range(min_val, max_val+1)]

# 再検証
K, X = map(int, input().split())
ans = ' '.join(map(str, range(X-K+1, X+K)))
print(ans)
