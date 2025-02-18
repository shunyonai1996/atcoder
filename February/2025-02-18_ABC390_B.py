import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))

if N == 2:
    print("Yes")
else:
    x = A[1] / A[0]
    check_list = [A[i-1] * x for i in range(1,N)]
    check_list.insert(0,A[0])
    if check_list == A:
        print('Yes')
    else:
        print('No')