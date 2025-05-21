s = input().split()
A = int(s[0])
B = s[1].split('.')

print(A * (int(B[0]) * 100 + int(B[1].ljust(2, '0'))) // 100)