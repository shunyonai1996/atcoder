import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

A, B, C, X = [int(input()) for _ in range(4)]
ans = 0

for a in range(min(A+1, X//500+1)):
    value_a = X - 500 * a
    for b in range(min(B+1, value_a//100+1)):
        value_b = value_a - 100 * b
        if value_b // 50 <= C:
            ans += 1
print(ans)

# AIによる数学的アプローチの別解
A, B, C, X = [int(input()) for _ in range(4)]
ans = 0

for a in range(min(A+1, X//500 + 1)):
    for b in range(min(B+1, (X - 500*a)//100 + 1)):
        c_needed = (X - 500*a - 100*b) // 50
        if (X - 500*a - 100*b) % 50 == 0 and 0 <= c_needed <= C:
            ans += 1

print(ans)