import io,sys
with open("input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

A, B = map(str, input().split())

a, b = 0, 0
for i in range(3):
    a += int(A[i])
    b += int(B[i])

print(b) if a < b else print(a)