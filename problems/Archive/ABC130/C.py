import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

W, H, x, y = list(map(int, input().split()))

sep_min_x = min([x * H] + [(W - x) * H])
sep_min_y = min([W * y] + [W * (H - y)])
max_num = max(sep_min_x, sep_min_y)

if sep_min_x == sep_min_y and (x == 0 and y == 0):
    print(str('{:.07f}'.format(max_num)) + ' 1')
else:
    print(str('{:.07f}'.format(max_num)) + ' 0')

# AIの解説後再解答
W, H, x, y = list(map(int, input().split()))

min_size = W * H / 2

if (W / 2, H / 2) == (x, y):
    print(str('{:.7f}'.format(min_size)) + ' 1')
else:
    print(str('{:.7f}'.format(min_size)) + ' 0')
