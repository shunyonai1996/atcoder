import re
X = input()

print(re.sub(r'\..*$', '', X))