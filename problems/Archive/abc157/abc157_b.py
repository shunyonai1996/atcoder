a = [list(map(int, input().split())) for v in range(3)]
n = int(input())

for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if b == a[j][k]:
                a[j][k] = 'c'

for i in range(3):
    yoko = True
    tate = True
    for j in range(3):
        if a[i][j] != 'c':
            yoko = False
        if a[j][i] != 'c':
            tate = False
    if yoko or tate:
        print('Yes')
        exit()
if (a[0][0] == a[1][1] and a[1][1] == a[2][2]) or (a[0][2] == a[1][1] and a[1][1] == a[2][0]):
    print('Yes')
else:
    print('No')