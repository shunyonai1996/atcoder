import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
stuck_p = 0

# N:勇者 N+1:街 A[i]:街にいる怪獣の数 B[i]:勇者の戦闘力
# 街N[i] -> A[i]体の怪獣がいる -> 勇者N[i]がB[i]体の怪獣を消すmax(0,A[i]-B[i])
# 街N[i+1] -> A[i+1]体の怪獣がいる -> 0<B[i]なら勇者N[i]がB[i+1]-max(0, (B[i]-(A[i]-B[i])))体の怪獣を消す
# → かつ勇者N[i]がB[i+1]体の怪獣を消すmax(0,A[i+1]-B[i]+1)

for i in range(N):
    ans += min(A[i], B[i]+stuck_p)
    stuck_p = max(0, B[i]+stuck_p-A[i])

if 0 < stuck_p:
    ans += min(A[N-1], stuck_p)

print(ans)