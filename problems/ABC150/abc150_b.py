N = int(input())
S = input()

ans = 0
for i in range(N-2):
    print(S[i:i+2],S[i:i+3])
    if S[i:i+3] == "ABC":
        ans += 1
print(ans)