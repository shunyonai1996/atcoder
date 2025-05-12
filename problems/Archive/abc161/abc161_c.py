M, K = map(int, input().split())

if M > K:
    a = M // K
    b = M - K * a
    print(min(b, abs(b - K)))
elif M < K:
    x = abs(M - K)
    print(min(x, M))
else:
    print('0')

# AIによる別解
N, K = map(int, input().split())

r = N % K
print(min(r, abs(K - r)))