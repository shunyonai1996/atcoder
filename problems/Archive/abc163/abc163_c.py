import collections
N = int(input())
A = list(map(int, input().split()))
ans = [0] * N

for item in collections.Counter(A).items():
    ans[item[0]-1] = item[1]

for i in ans:
    print(i)