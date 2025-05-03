import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
A,B,C = [list(map(int, input().split())) for _ in range(3)]
score = 0
tp = 100

for i in range(N):
    score += B[A[i]-1]
    if tp == A[i]-1:
        score += C[tp-1]
    tp = A[i]
print(score)