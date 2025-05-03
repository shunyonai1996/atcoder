import io,sys
with open("/Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N = int(input())
min_point = float('inf')
prime = prime_factorize(N)

for i in range(1, len(prime)):
    l = 1
    r = 1
    for j in prime[i:]:
        l *= j
    for j in prime[:i]:
        r *= j
    min_point = min(min_point, l-1 + r-1)

print(N-1) if min_point == float('inf') else print(min_point)