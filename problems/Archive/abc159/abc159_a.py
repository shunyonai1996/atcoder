N, M = map(int, input().split())
even_pairs = N * (N - 1) // 2
odd_pairs = M * (M - 1) // 2
print(even_pairs + odd_pairs)