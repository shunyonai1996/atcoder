import io,sys
with open("../input.txt") as TxtOpen:
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
# 着けているゼッケンにかかれている数(Q[P[i]])をSiとする。

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

print(N,P,Q)

# 1番さん=>2=>4番さん=>4
# 2番さん=>3=>3番さん=>1
# 3番さん=>1=>2番さん=>3
# 4番さん=>4=>1番さん=>2