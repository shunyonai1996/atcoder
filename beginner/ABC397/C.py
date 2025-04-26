import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# N = int(input())
# A = list(map(int, input().split()))

# ans = 0
# for i in range(N):
#     if ans < len(set(A[:i])) + len(set(A[i:])):
#         ans = len(set(A[:i])) + len(set(A[i:]))
# print(ans)


# 解説
# 事前にprefixとsuffixのリストを作成し、i回目とi+1回目の種類数を作成しておく
# のぞいたそれぞれのリストを使ってN回ループを回す。
# 区切った位置の中で種類が最大になるパターンを抽出

N = int(input())
A = list(map(int, input().split()))

seen = set()
prefix = [0] * (N)
count = 0
for i in range(N):
    if A[i] not in seen:
        seen.add(A[i])
        count += 1
    prefix[i] = count

# 今回は以下のコメントアウトの記載でも同様の結果が得られる
# ※ただし、累積和の計算によっては結果が異なるケースもあるため非推奨
# suffix = list(reversed(prefix))
seen = set()
suffix = [0] * (N)
count = 0

for i in range(N-1, -1, -1):
    if A[i] not in seen:
        seen.add(A[i])
        count += 1
    suffix[i] = count
    print(i)
    print(seen)
    print(suffix)

print(prefix,suffix)
ans = 0
for i in range(N-1):
    ans = max(ans, prefix[i] + suffix[i+1])
print(ans)