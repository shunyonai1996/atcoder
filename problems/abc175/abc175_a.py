S = input()
ans = 0

cnt = S.count('R')
if cnt == 2:
    if S[1] == "R":
        print(2)
        exit()
    else:
        print(1)
        exit()

print(cnt)