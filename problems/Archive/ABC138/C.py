import io,sys
with open("/Users/crudist_yonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
V = sorted(map(int, input().split()))
max_val = 0
calc_val = V[0]

for i in range(1, N):
    calc_val = (calc_val + V[i]) / 2
    max_val = max(max_val, calc_val)
print(max_val)