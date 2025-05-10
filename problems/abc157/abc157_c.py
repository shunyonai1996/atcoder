n, m = map(int, input().split())
sc = [list(map(int, input().split())) for i in range(m)]

ans = '-1'
for i in range(0, 1000):
    v = str(i)
    check = True
    if len(v) != n:
        continue
    for j in range(m):
        s, c = sc[j]
        if s == 1 and c == 0:
            if n == 1:
                print('0')
            else:
                print('-1')
            exit()
        if v[s-1] != str(c):
            check = False
            break
    if check:
        ans = v
        break
print(ans)



# ans = [-1] * n

# for _ in range(m):
#     s, c = map(int, input().split())
#     pos = s - 1
#     if pos == 0 and c == 0 and n > 1:
#         print('-1')
#         exit()
#     if ans[pos] != -1 and ans[pos] != c:
#         print(-1)
#         exit()
#     ans[pos] = c

# for i in range(n):
#     if ans[i] == -1:
#         if i == 0:
#             ans[i] = 1 if n > 1 else 0
#         else:
#             ans[i] = 0

# ans = ''.join(map(str, ans))
# print(ans) if len(ans) == n else print('-1')