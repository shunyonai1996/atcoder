import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue整理
# 回答を逆算する
# 1からnまでループで全て掛けていき、inputとi番目のループが一致した時点でprint

X = int(input())
n = 1
for i in range(1,X+1):
    n*=i
    if X == n:
        print(i)
        break