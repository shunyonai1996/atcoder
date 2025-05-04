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


# 解説
N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

def right_rot90(S):
  return list(zip(*S[::-1]))

def count_diff(S,T):
  return sum([1 for si,ti in zip(S,T) for sij,tij in zip(si,ti) if sij!=tij])

ans = 10**9
for rot_count in range(4):
  ans = min(ans, count_diff(S,T)+rot_count)
  S = right_rot90(S)

print(ans)
