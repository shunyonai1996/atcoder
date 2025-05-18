K = int(input())
A, B = map(int, input().split())

i = 1
while i * K <= 1000:
    if A <= i * K <= B:
        print('OK')
        exit()
    i += 1
print('NG')