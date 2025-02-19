import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue

# 条件分岐
# 三つの文字が違う文字列である場合
# かつ、文字列内が等間隔であること j−i=k−j

S = str(input())
list = list(S)

for i in range(0, len(S)-1):
    list[i]==list[i+1]
    print(list[i])


1 1111111 1 1111111 1