from math import gcd

K = int(input())
total = 0

for a in range(1, K + 1):
    for b in range(1, K + 1):
        ab_gcd = gcd(a, b)
        for c in range(1, K + 1):
            total += gcd(ab_gcd, c)

print(total)