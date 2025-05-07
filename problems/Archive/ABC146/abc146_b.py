N = int(input())
S = list(input())

ans = []
for char in S:
    idx = ord(char) - ord('A')
    new_v = chr(ord('A') + (idx + N) % 26)
    ans.append(new_v)

print(''.join(ans))