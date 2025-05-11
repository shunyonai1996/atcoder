X = int(input())

a = X // 500
b = (X - (X // 500 * 500)) // 5

print(a * 1000 + b * 5)