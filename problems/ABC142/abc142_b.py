N, K = list(map(int, input().split()))
H = map(int, input().split())

ans = 0
for i in H:
  if K <= i:
    ans += 1

print(ans)