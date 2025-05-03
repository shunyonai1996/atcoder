import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# def prime_factorize(n):
#     a = []
#     while n % 2 == 0:
#         a.append(2)
#         n //= 2
#     f = 3
#     while f * f <= n:
#         if n % f == 0:
#             a.append(f)
#             n //= f
#         else:
#             f += 2
#     if n != 1:
#         a.append(n)
#     return a

# N = int(input())
# min_point = float('inf')
# prime = prime_factorize(N)

# for i in range(1, len(prime)):
#     for j in range(1, len(prime)):
        
#         min_point = min(min_point, l-1 + r-1)

# print(N-1) if min_point == float('inf') else print(min_point)


# AIの回答
import sys

def prime_factorize(n):
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        print(factors)
        n //= 2
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors[f] = factors.get(f, 0) + 1
            n //= f
            print(factors)
        f += 2
    if n != 1:
        factors[n] = 1
    return factors

N = int(sys.stdin.readline())
if N == 1:
    print(0)
    sys.exit()

factors = prime_factorize(N)
divisors = [1]
for p, cnt in factors.items():
    temp = []
    for d in divisors:
        current = d
        for e in range(1, cnt + 1):
            current *= p
            temp.append(current)
    divisors += temp

min_val = float('inf')
for d in divisors:
    other = N // d
    min_val = min(min_val, d + other - 2)

print(min_val)