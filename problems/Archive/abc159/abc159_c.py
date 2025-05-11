from fractions import Fraction

L = float(input())
a = Fraction(L / 3) ** 3
print("{:.12f}".format(float(a)))