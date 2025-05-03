import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

S = int(input())
list_ = [i for i in map(int, input().split())]
print(sum([list_[i-1] for i in range(1, S+1) if i%2 != 0]))