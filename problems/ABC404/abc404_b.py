N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]
min_cnt = float('inf')

for c in range(4):
  cnt = c
  for i in range(N):
    for j in range(N):
      if S[i][j] != T[i][j]:
        cnt+=1
  tmp_S = [row[:] for row in S]
  for i in range(N):
    for j in range(N):
      tmp_S[i][j] = S[j][i]
    tmp_S[i] = tmp_S[i][::-1]
  S = tmp_S = [row[:] for row in tmp_S]
  min_cnt = min(min_cnt, cnt)

print(min_cnt)