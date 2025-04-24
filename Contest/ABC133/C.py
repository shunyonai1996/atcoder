import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# Lが2019未満 Rが2019未満
# Lが2019未満 Rが2019以上
# Lが2019以上 Rが2019未満
# Lが2019以上 Rが2019以上

L, R = map(int, input().split())
min_val = 2019
print(47*48%2019)
# i, i+1はWA
# i, i+nにすること

for i in range(L, R):
    min_val = min(min_val, (i * (i + 1)) % 2019)
    if min_val == 0:
        break

print(min_val)