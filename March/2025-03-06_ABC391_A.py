import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

D = input()

if D == 'N':
    print('S')
elif D == 'S':
    print('N')
elif D == 'E':
    print('W')
elif D == 'W':
    print('E')
elif D == 'NE':
    print('SW')
elif D == 'SW':
    print('NE')
elif D == 'NW':
    print('SE')
elif D == 'SE':
    print('NW')