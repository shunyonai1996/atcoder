n, k = map(int, input().split())

def base_digit_count(n, k):
    count = 0
    while n:
        count += 1
        print(f"bf:{n}")
        n //= k
        print(f"af:{n}")
    return count

print(base_digit_count(n, k))