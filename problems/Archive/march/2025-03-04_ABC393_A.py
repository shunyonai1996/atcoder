import io,sys
with open("/Users/shunyonai/Documents/GitHub/atcoder/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# sick sick -> 1が毒
# sick fine -> 2が毒
# fine sick -> 3が毒
# fine fine -> 4が毒

S = input()

if S == 'sick sick':
    print(1)
elif S == 'sick fine':
    print(2)
elif S == 'fine sick':
    print(3)
elif S == 'fine fine':
    print(4)