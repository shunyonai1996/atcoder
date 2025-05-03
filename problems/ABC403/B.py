import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

T = list(input())
S = list(input())

ans = 'Yes'
for i in range(len(T)-len(S)+1):
    ok = True
    for j in range(len(S)):
        if T[i+j] != S[j] and T[i+j] != '?':
            ok = False
            ans = 'No'
            break
    if ok:
        ans = 'Yes'
        break
print(ans)