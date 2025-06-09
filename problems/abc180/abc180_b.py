import math
N = int(input())
X = list(map(int, input().split()))

print(sum(abs(x) for x in X))
print(math.sqrt(sum(abs(x)**2 for x in X)))
print(max(abs(x) for x in X))