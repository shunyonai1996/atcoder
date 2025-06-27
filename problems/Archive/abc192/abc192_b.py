S = input()
ans = 'Yes'

for i in range(len(S)):
    if (i % 2 == 0 and S[i] != S[i].lower()) \
       or (i % 2 == 1 and S[i] != S[i].upper()):
        ans = 'No'

print(ans)