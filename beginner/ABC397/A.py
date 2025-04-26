import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

X = float(input())
if 38 <= X:
    print(1)
elif 37.5 <= X < 38:
    print(2)
else:
    print(3)