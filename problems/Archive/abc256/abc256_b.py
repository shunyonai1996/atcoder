N = int(input())
A = list(map(int, input().split()))
B = [0] * 4
P = 0

for i in range(N):
    B[0] = 1
    for j in range(3, -1, -1):
        if B[j] == 1:
            if j + A[i] < 4:
                B[j] = 0
                B[j + A[i]] = 1
            else:
                P += 1
                B[j] = 0
print(P)