n = int(input())
x = list(map(int, input().split()))
min_dis = float('inf')

for p in range(min(x), max(x)+1):
    dis = 0
    for xi in x:
        dis += (xi - p) ** 2
    min_dis = min(dis, min_dis)
print(min_dis)