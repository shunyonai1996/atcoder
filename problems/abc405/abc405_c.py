N = int(input())
A = list(map(int, input().split()))

square_sum = sum(x**2 for x in A)
ans = (sum(A)**2 - square_sum) // 2

print(ans)