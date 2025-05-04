N = int(input())
S = list(input())

for i in range(N):
  for j in range(N):
    if S[:i] and S[i:]:
      if ''.join(S[:i]) == ''.join(S[i:]):
        print('Yes')
        exit()
print('No')