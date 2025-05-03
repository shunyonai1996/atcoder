import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, K = list(map(int, input().split()))
S = list(input())
S[K-1] = S[K-1].lower()
print(''.join(S))