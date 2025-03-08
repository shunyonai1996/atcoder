import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# issue
# YY => 00~99まで可能
# MM => 01~12まで可能（つまりYYも可能性がある）
# S[0]が00 or 13以上、かつS[1]が01~12の組み合わせ→YYMM
# S[0]が01~12、かつS[1]が00 or 13以上の組み合わせ→MMYY
# S[0]、S[1]がともに01~12→AMBIGUOUS
# S[0]、S[1]がともに00 or 13以上→NA
# 出力パターン YYMM, MMYY, AMBIGUOUS, NA

# AIによるソースレビュー
# リスト表記はメモリ効率が悪いため、単一の整数を二つ定義すべき
# 比較演算子の記法を統一する

S = input()
list_ = [int(S[i:i+2]) for i in range(0,4,2)]

if (list_[0] == 0 or 13 <= list_[0]) and 1 <= list_[1] <= 12:
    print('YYMM')
elif 1 <= list_[0] <= 12 and (0 == list_[1] or 13 <= list_[1]):
    print('MMYY')
elif 1 <= list_[0] <= 12 and 1 <= list_[1] <= 12:
    print('AMBIGUOUS')
else:
    print('NA')


# AI提供のソースコード
S = input()

# スライスの省略記法S[:2],S[2:]
first = int(S[:2])
second = int(S[2:])

if (first == 0 or first >= 13) and 1 <= second <= 12:
    print('YYMM')
elif 1 <= first <= 12 and (second == 0 or second >= 13):
    print('MMYY')
elif 1 <= first <= 12 and 1 <= second <= 12:
    print('AMBIGUOUS')
else:
    print('NA')

# AI提供の最大限記述を簡略化
S=input()
a,b=int(S[:2]),int(S[2:])
if(a==0 or a>12)and 0<b<13:print('YYMM')
elif 0<a<13 and(b==0 or b>12):print('MMYY')
elif 0<a<13 and 0<b<13:print('AMBIGUOUS')
else:print('NA')