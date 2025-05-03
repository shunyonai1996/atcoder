import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# Pは人
# Qはiさんの番号
# i番さんとゼッケン番号と見てる人の番号 i Q[i]
# 見られてる人のゼッケン番号はQ[P[i]]

# iが書かれたゼッケンを着けている人(Q[i])が
# 見つめている人(P[i])の
# 着けているゼッケンにかかれている数(Q[P[i]])をSiとする

N = int(input())
P=[0]+list(map(int,input().split()))
Q=[0]+list(map(int,input().split()))
S = []

print(N,P,Q,ans_list)

for i in range(N):
    print(P[i])
    ans_list[Q[i]-1] = Q[P[i-1]-1]

ans=[0]*(N+1)
for i in range(1,N+1):
  print(Q[i])
  print(Q[P[i]])
  ans[Q[i]]=Q[P[i]]
  print(ans)

print(*ans[1:])