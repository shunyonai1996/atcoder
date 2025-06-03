import io,sys
with open("input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

S = input()
T = input()
ans = 0

if len(S) == len(T):
    cnt = 0
    for i in range(len(S)):
        if S[i] == T[i]:
            cnt += 1
    ans = max(ans, cnt)
else:
    for i in range(len(S)-len(T)):
        cnt = 0
        for j in range(len(T)):
            if S[i + j] == T[j]:
                cnt += 1
        ans = max(ans, cnt)

print(len(T) - ans)