import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

S = input()
week_list = ['SUN','MON','TUE','WED','THU','FRI','SAT']

ans = 7
for v in week_list:
    if S == v:
        print(ans)
    ans -= 1