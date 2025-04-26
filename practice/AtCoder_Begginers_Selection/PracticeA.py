import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# nums = sum(list(x for _ in range(2) for x in map(int, input().split())))
# print(f"{str(nums)} {input()}")

a = int(input())
b, c = map(int, input().split())
s = input()

print("{} {}".format(a+b+c, s))