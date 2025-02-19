import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# 各グリッドに入るリストを準備
# 入力と一致する値をリストから全て除外
# 除外後、リスト内の要素を全て足し合わせる

X = int(input())
grid = [i*j for j in range(1,10) for i in range(1,10)]
total = sum([grid[i] for i in range(0, len(grid)) if X != grid[i]])

print(total)