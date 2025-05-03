import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import sys
input = sys.stdin.readline

N = int(input())
ans = [0] * N
A = list(map(int, input().split()))

for i in range(1, N+1):
    # i番目=ついた順
    # A[i-1]=ついた人の名前
    ans[A[i-1]-1] = i

print(' '.join([str(i) for i in ans]))

# AIの別解
students = sorted([(A[i], i+1) for i in range(N)])
print(' '.join(str(s[1]) for s in students))