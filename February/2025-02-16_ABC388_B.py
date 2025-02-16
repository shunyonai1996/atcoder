import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue整理
# N D 蛇の数 出力する行数
# TL 蛇ごとの情報をリストで持つ
# 蛇重さは太さと長さの積（Dの長さがk伸びる）
# k行目のループで各蛇の重さを計算し、maxの蛇の重さをprint

N, D = map(int, input().split())
TL = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, D+1):
    calc_arr = []
    for a in range(len(TL)):
        calc_arr.append((TL[a][1] + i) * TL[a][0])
    print(max(calc_arr))