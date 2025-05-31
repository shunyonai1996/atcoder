N = int(input())
A = list(map(int, input().split()))

print(len(set(A)))
print(' '.join(map(str, sorted(set(A)))))