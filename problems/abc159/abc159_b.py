S = input()

pre_s = S[:(len(S) - 1) // 2]
suf_s = S[(len(S) + 3) // 2 - 1:]

if S == S[::-1] and pre_s == pre_s[::-1] and suf_s == suf_s[::-1]:
    print('Yes')
else:
    print('No')