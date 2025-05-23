import string
N, X = list(map(int, input().split()))
char = ''
for c in list(string.ascii_uppercase):
    char += c * N

print(char[X-1])