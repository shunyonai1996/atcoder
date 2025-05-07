N = int(input())
S = input()

ans = 0
for i in range(N-2):
    if ''.join(S[i:i+3]) == 'ABC':
        ans += 1

print(ans)