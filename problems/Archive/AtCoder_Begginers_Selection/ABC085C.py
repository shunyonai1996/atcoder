import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, Y = list(map(int, input().split()))

x_ans,y_ans,z_ans = [-1] * 3
for x in range(min(N, Y//10000)+1):
    used_money_x = Y - x * 10000

    if used_money_x == 0 and x == N:
        x_ans,y_ans,z_ans = [x, 0, 0]
        break

    for y in range(min(N-x, used_money_x//N-x)+1):
        used_money_y = used_money_x - y * 5000
        if used_money_y == 0 and x + y == N:
            x_ans,y_ans,z_ans = [x, y, 0]
            break

        if used_money_y - 1000 * (N-x-y) == 0:
            x_ans,y_ans,z_ans = [x, y, N - x - y]
            break

print(x_ans,y_ans,z_ans)

# AIによる別解
# 計算量を2000*2000で許容できるなら、ロジックを減らして実装速度を上げるという指針に基づく
N, Y = map(int, input().split())

for x in range(N + 1):
    for y in range(N - x + 1):  # x + y <= N を保証
        z = N - x - y
        total = 10000 * x + 5000 * y + 1000 * z
        if total == Y:
            print(x, y, z)
            exit()

print(-1, -1, -1)