import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
pt, px, py = 0, 0, 0
ans='Yes'

for _ in range(N):
    ti, xi, yi = map(int, input().split())
    dt = ti - pt
    distance = abs(px-xi)+abs(py-yi)
    if dt < distance or (dt - distance) % 2 != 0:
        ans = 'No'
        break
    pt, px, py = ti, xi, yi
print(ans)