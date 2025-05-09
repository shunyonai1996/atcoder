# a, b, c = map(int, input().split())

# if (a == b and a != c) or (b == c and a != b) or (a == c and c != b):
#     print('Yes')
# else:
#     print('No')

print('Yes') if len(set(map(int,input().split()))) == 2 else print('No')