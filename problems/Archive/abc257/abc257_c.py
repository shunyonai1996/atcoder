# N = int(input())
# S = input()
# W = list(map(int, input().split()))

# adult = S.count('1')
# child = N - adult
# if adult == 0 or child == 0:
#     print(N)
#     exit()

# base_weight = sorted(W)[child]
# _base_weight = base_weight - 1
# base_weight_ = base_weight + 1
# _ans = 0
# ans = 0
# ans_ = 0

# for i in range(N):
#     w = W[i]
#     s = S[i]
#     if w < base_weight and s == '0':
#         ans += 1
#     elif w >= base_weight and s == '1':
#         ans += 1

#     if w < _base_weight and s == '0':
#         _ans += 1
#     elif w >= _base_weight and s == '1':
#         _ans += 1

#     if w < base_weight_ and s == '0':
#         ans_ += 1
#     elif w >= base_weight_ and s == '1':
#         ans_ += 1

# print(max(_ans, ans, ans_))

N = int(input())
S = input()
W = list(map(int, input().split()))

# 人の情報をまとめる（体重と0/1ラベル）
people = [(W[i], S[i]) for i in range(N)]
# 体重でソート
people.sort()

adult_count = S.count('1')
child_count = N - adult_count
score = adult_count
ans = score

for i in range(N):
    weight, label = people[i]
    if label == '1':
        score -= 1
    else:
        score += 1

    # 次の人と体重が同じなら境界は変わらないので skip
    if i < N - 1 and people[i][0] == people[i + 1][0]:
        continue
    ans = max(ans, score)

print(ans)
