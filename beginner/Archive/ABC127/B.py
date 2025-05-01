import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

r, D, x = list(map(int, input().split()))
weight = x

for i in range(10):
    weight = r * weight - D
    print(weight)


# 別解1：リスト内包表記を使用
r, D, x = map(int, input().split())
x_list = [x]
[print(x_list.append(r * x_list[-1] - D) or x_list[-1]) for _ in range(10)]

# 別解2：再帰関数を使用
def calc_next(r, D, x, count=0):
    if count == 10:
        return
    next_x = r * x - D
    print(next_x)
    calc_next(r, D, next_x, count + 1)

r, D, x = map(int, input().split())
calc_next(r, D, x)

# 別解3：functools.reduceを使用
from functools import reduce

r, D, x = map(int, input().split())
reduce(lambda acc, _: print(r * acc - D) or r * acc - D, range(10), x)
