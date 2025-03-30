import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

S = sorted(list(str(input())))

if S[0] == S[1] and S[1] != S[2] and S[2] == S[3]:
    print('Yes')
else:
    print('No')