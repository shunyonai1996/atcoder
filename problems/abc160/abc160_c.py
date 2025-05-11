# 直線 0----5----10----15----20
# K - max(0とNの距離, それ以外の距離の最大値)

K, N = map(int, input().split())
A = list(map(int, input().split()))

a  = K - A[-1] + A[0]
max_distance = 0

for i in range(1, N):
    distance = A[i] - A[i-1]
    max_distance = max(max_distance, distance)
print(K - max(a, max_distance))