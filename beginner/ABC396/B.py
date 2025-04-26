import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

Q = int(input())
C = [list(map(int, input().split())) for _ in range(Q)]
cards = [0]

for i in range(Q):
    if C[i][0] == 2:
        if len(cards) == 1:
            print(cards[-1])
        else:
            print(cards[-1])
            cards.pop(-1)
    else:
        cards.append(C[i][1])


# 解説の解答
# スタックを使用する問い
# ループの中でqueryを呼び出す方が配列を格納しなくて良いし、直感的
stack = []
for _ in range(100):
    stack.append(0)
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        stack.append(x)
    else:
        print(stack.pop())
