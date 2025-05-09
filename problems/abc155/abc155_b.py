N = int(input())
A = [i for i in map(int, input().split()) if i % 2 == 0]

for i in A:
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print('DENIED')
        exit()

print('APPROVED')