import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
ans = ['-'] * N

if N % 2 == 0:
    ans[int(N / 2) - 1] = '='
    ans[int(N / 2)] = '='
else:
    ans[int((N-1) / 2)] = '='

print(''.join(ans))

# 解説記事
# アプローチほぼ同じ
# N=int(input())

# if N%2==0:
#   c = (N-2)//2
#   print('-'*c + '='*2 + '-'*c)
# else:
#   c = (N-1)//2
#   print('-'*c + '=' + '-'*c)
