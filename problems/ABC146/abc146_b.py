import string
alphabet = string.ascii_uppercase * 2
N = int(input())
S = list(input())

ans = []
for char in S:
    ans.append(alphabet[alphabet.index(char)+N])

print(''.join(ans))