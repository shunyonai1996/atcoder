import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

S = input()

if S == 'Sunny':
    print('Cloudy')
elif S == 'Cloudy':
    print('Rainy')
else:
    print('Sunny')
