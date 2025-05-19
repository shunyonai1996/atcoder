K = int(input())
S = list(input())

if K < len(S):
    ans = S[:K]
    ans.append('...')
    print(''.join(map(str, ans)))
else:
    print(''.join(map(str, S)))