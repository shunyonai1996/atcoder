import io,sys
with open(".//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

def main():
    num_list = [1,2,3]
    input_list = {int(input()) for _ in range(2)}
    ans = [v for v in num_list if v not in input_list]
    print(ans[0])

if __name__ == "__main__":
    main()