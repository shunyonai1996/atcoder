N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]
S2 = [['.'] * N for _ in range(N)]
S3 = [['.'] * N for _ in range(N)]
S4 = [['.'] * N for _ in range(N)]

for i in range(N):
  for j in range(N):
    S2[i][j] = S[j][i]
S2 = [list(row)[::-1] for row in S2]

for i in range(N):
  for j in range(N):
    S3[i][j] = S2[j][i]
S3 = [list(row)[::-1] for row in S3]

for i in range(N):
  for j in range(N):
    S4[i][j] = S3[j][i]
S4 = [list(row)[::-1] for row in S4]

min_cnt = float('inf')

cnt = 0
for i in range(N):
  for j in range(N):
    if S[i][j] != T[i][j]:
      cnt+=1
min_cnt = min(min_cnt, cnt)

cnt = 1
for i in range(N):
  for j in range(N):
    if S2[i][j] != T[i][j]:
      cnt+=1
min_cnt = min(min_cnt, cnt)

cnt = 2
for i in range(N):
  for j in range(N):
    if S3[i][j] != T[i][j]:
      cnt+=1
min_cnt = min(min_cnt, cnt)

cnt = 3
for i in range(N):
  for j in range(N):
    if S4[i][j] != T[i][j]:
      cnt+=1
min_cnt = min(min_cnt, cnt)

print(min_cnt)