import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数
# 計算量が多すぎてTLEとなる

A, B, C, D = list(map(int, input().split()))
a_to_b = B - A

# print(a_to_b)
ans = 0
if C == D:
    for v in range(A, B):
        if v % C == 0:
            ans += 1
else:
    for v in range(A, B):
        if v % C == 0 or v % D == 0:
            ans += 1

print(a_to_b - ans)