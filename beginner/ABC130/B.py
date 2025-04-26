import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N, X = list(map(int, input().split()))
L = [int(l) for l in list(input().split())]

pointer = 0
answer = 1

for i in range(N):
    pointer += L[i]
    if pointer <= X:
        answer += 1
    else:
        break

print(answer)