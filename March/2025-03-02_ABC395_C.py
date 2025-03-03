import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# ダブりが存在するかどうかを検証
# カウントアップしていき、重複が存在した時点の長さを保持
# ダブってる数値を洗い出す
# その中の距離が最小の長さを求める

N = int(input())
A = list(map(int, input().split()))

print(N, A)

dup_list = [e for e in set(A) if A.count(e) > 1]

print(dup_list)

for i in dup_list:
    print(i)
    # print(A[N-1-i])