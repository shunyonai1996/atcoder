a, b, c = map(int, input().split())

if (a <= b and b <= c) or (c <= b and b <= a):
    print('Yes')
else:
    print('No')