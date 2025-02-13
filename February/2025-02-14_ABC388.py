import io,sys
with open("../input.txt") as TxtOpen:
    INPUT=TxtOpen.read()
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

s = input()
upper_str = s[0]
print(f"{upper_str}UPC")

# AIの別解
# s = input()
# print(s[0] + "UPC")

# AIの別解
# s = input()
# print("{}UPC".format(s[0]))

# AIの別解
# s = input()
# print("%sUPC" % s[0])

# AIの別解
# print(input()[0] + "UPC")