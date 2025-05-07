import itertools
N = int(input())
d = list(map(int, input().split()))

ans = 0
for i in itertools.combinations(d, 2):
  ans += i[0] * i[1]
print(ans)