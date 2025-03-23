import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# AIによるソースレビュー

# N = sorted(list(map(int, input().split())))
N = list(map(int, input().split()))
T = [0]+[0] * 13

for i in N:
    T[i-1] += 1

x = False
y = False

for i in sorted(T):
    if 2 <= i <= 5 and x == False:
        x = True
    elif 3 <= i <= 5:
        y = True

if x and y:
    print('Yes')
else:
    print('No')


# AIによる別解
N = list(map(int, input().split()))
T = [0]*13

for i in N:
    T[i-1] += 1

found = False

# 全ての組み合わせを明示的に確認
for i in range(13):
    if T[i] >= 3:
        for j in range(13):
            if i != j and T[j] >= 2:
                found = True
                break
        if found:
            break

print('Yes' if found else 'No')