import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# N*Nのグラフをループで上書きしていく
# 決まった計算式を間違いなく作成できれば解ける
# 複数配列の決まった範囲の値を一括で書き換える方法がわからない

N = int(input())
grid = [['?'] * N for j in range(N)]

for i in range(1, N+1):
    j = N + 1 - i
    if i <= j:
        for x in range(i-1, j):
            for y in range(i-1, j):
                if i % 2 != 0:
                    grid[x][y] = '#'
                else:
                    grid[x][y] = '.'
    print(''.join(grid[i-1]))