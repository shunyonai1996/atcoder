S = input()
t = ['A','C','G','T']
cnt = 0
ans = 0

for i in range(len(S)):
    if S[i] in t:
        cnt +=1
    else:
        cnt = 0
    ans = max(cnt, ans)

print(ans)