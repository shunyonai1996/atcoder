# A, B, C = map(int, input().split())

# if C == 0:
#     while True:
#         A -= 1
#         if A == 0:
#             print("Aoki")
#             break
#         B -= 1
#         if B == 0:
#             print("Takahashi")
#             break
# else:
#     while True:
#         B -= 1
#         if B == 0:
#             print("Takahashi")
#             break
#         A -= 1
#         if A == 0:
#             print("Aoki")
#             break

# exit()
A, B, C = map(int, input().split())

if C == 0:
    if A == 0:
        print('Aoki')
        exit()
    if A <= 0 or B <= A - 1:
        print('Takahashi')
    else:
        print('Aoki')
else:
    if B == 0:
        print('Takahashi')
        exit()
    if B <= 0 or A <= B - 1:
        print('Aoki')
    else:
        print('Takahashi')