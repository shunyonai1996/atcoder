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