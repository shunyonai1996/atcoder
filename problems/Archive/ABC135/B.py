import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
P = list(map(int, input().split()))
diff_cnt = 0

for i in range(1, N+1):
    if i != P[i-1]:
        diff_cnt += 1
print('NO') if 3 <= diff_cnt else print('YES')

# AIによる別解
index_list = []
for i, v in enumerate(P, 1):
    if i != v:
        index_list.append((i, v))
# Check if the number of mismatched pairs is 2 or less
if len(index_list) == 0:
    print('YES')  # Already sorted
elif len(index_list) == 2:
    # Check if swapping the two mismatched elements sorts the array
    (i1, v1), (i2, v2) = index_list
    if i1 == v2 and i2 == v1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
