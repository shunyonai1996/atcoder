import collections
N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)
    exit()

ans = 1
for item in collections.Counter(A).items():
    i, c = item
    ans *= i ** c
    if 10 ** 18 < ans:
        print(-1)
        exit()

print(ans)