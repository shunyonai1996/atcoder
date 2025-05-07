A, B = map(int, input().split())

def lcm_r(a, b):
    remainder = a % b
    if remainder == 0:
        return a
    return a * lcm_r(b, remainder) / remainder

v = lcm_r(A, B)
print(int(v))