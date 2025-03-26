import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

W, H, x, y = list(map(int, input().split()))

sep_min_x = min([x * H] + [(W - x) * H])
sep_min_y = min([W * y] + [W * (H - y)])
max_num = max(sep_min_x, sep_min_y)

if sep_min_x == sep_min_y and (x != 0 and y != 0):
    print(str('{:.07f}'.format(max_num)) + ' 1')
else:
    print(str('{:.07f}'.format(max_num)) + ' 0')