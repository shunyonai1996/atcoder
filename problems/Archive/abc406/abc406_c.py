n = int(input())
p = list(map(int, input().split()))

# 1. 隣接ペアごとの「<」「>」列を作る
s = []
for i in range(n - 1):
    if p[i] < p[i + 1]:
        s.append('<')
    else:
        s.append('>')

# 2. ランレングス圧縮（RLE）
v = []
print(s)
for c in s:
    if not v or v[-1][0] != c:
        v.append([c, 1])
    else:
        v[-1][1] += 1

# 3. "<"×">"×"<" に該当するパターンを数え上げ
ans = 0
print(v)
for i in range(1, len(v) - 1):
    print(f"i:{i}")
    if v[i][0] == '>':
        print(f"v[i-1][1]: {v[i-1][1]}, v[i+1][1]: {v[i+1][1]}")
        ans += v[i-1][1] * v[i+1][1]
        print(ans)
print(ans)
