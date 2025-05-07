S = list(input())

for i, v in enumerate(S):
  if i % 2 == 0 and v in 'RUD':
    continue
  elif i % 2 != 0 and v in 'LUD':
    continue
  else:
    print('No')
    exit()

print('Yes')