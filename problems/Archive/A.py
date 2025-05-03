import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, A, B = map(int, input().split())
[print(index+1) for index, ans in enumerate(list(map(int, input().split()))) if ans == A + B]
