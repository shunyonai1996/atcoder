N = int(input())

ans = []
for i in range(N):
    row = []
    for j in range(i+1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(ans[i-1][j-1] + ans[i-1][j])
    ans.append(row)

for row in ans:
    print(' '.join(map(str, row)))