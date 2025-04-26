import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
S = list(input())

counter = 0
for i in range(len(S)):
    if S[i-1] == '2':
        counter += 1

answer = '2' * counter
print(answer)