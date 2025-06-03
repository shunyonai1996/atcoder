S = input()
T = input()

cnt = 0
for i in range(len(S)):
    tmp_cnt = 0
    for j in range(len(T)):
        for k in range(len(T)-j):
            if i+k <= len(S)-1 and j+k <= len(T)-1:
                if T[j+k] == S[i+k]:
                    tmp_cnt += 1
    cnt = max(cnt, tmp_cnt)

print(len(T) - cnt)