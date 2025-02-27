import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

S = sorted(list(map(int,input().split())))

print('Yes') if S[0] + S[1] == S[2] else (print('Yes') if S[0] == S[1] == S[2] else print('No'))