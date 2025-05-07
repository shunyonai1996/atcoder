N = int(input())
S, T = map(str, input().split())

char = ''
for i in range(N):
    char += S[i]+T[i]

print(char)