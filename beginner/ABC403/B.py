import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/beginner/ABC403/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

T = list(input())
S = list(input())

ans = 'Yes'
for i in range(len(T)-len(S)+1):
    flg = True
    for j in range(len(S)):
        if T[i+j] == S[j] or T[i+j]=='?':
            continue
        else:
            flg=False
    if flg == False:
        ans = 'No'
    else:
        ans = 'Yes'
        break
print(ans)