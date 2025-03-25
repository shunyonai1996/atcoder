import io,sys
with open("./input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

S = list(map(int, input()))
ans = 'Good'

for i in range(len(S)-1):
    if S[i] == S[i+1]:
        ans = 'Bad'
print(ans)