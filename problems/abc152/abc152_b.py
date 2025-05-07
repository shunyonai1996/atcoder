a, b = map(int, input().split())
ab = str(a) * b
ba = str(b) * a

if ab[0] < ba[0]:
    print(ab)
else:
    print(ba)