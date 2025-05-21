A, B = input().split()
A = int(A)
B = B.split('.')
if len(B) == 1:
    B = int(B[0]) * 100
else:
    B = int(B[0]) * 100 + int(B[1].ljust(2, '0'))

print(A * B // 100)
