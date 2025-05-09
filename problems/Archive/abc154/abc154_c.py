N = int(input())
A = len(set(map(int, input().split())))

print('NO') if N != A else print('YES')