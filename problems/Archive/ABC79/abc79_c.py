A, B, C, D = map(int, input())
for bit in range(2 ** 3):
    char_list = ['-'] * 3
    for i in range(3):
        if (bit >> i) & 1:
            char_list[i] = '+'
    expression = f"{A} {char_list[0]} {B} {char_list[1]} {C} {char_list[2]} {D}"
    if eval(expression) == 7:
        print(f"{''.join(expression.split())}=7")
        exit()


# AIの別解
l = [int(i) for i in map(str, input())]
ops = ['-', '+']
for ops1 in ops:
    for ops2 in ops:
        for ops3 in ops:
            expression = f"{l[0]}{ops1}{l[1]}{ops2}{l[2]}{ops3}{l[3]}"
            if eval(expression) == 7:
                print(expression+"=7")
                exit()