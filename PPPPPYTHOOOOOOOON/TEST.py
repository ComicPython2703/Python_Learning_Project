# coding=utf-8
import fractions
ftest11 = fractions.Fraction(int(input("分子：")), int(input('分母：')))
ftest12 = fractions.Fraction(int(input("分子：")), int(input('分母：')))
ftest0 = input("输入符号：")
if ftest0 == "+":
    print(ftest11 + ftest12)
elif ftest0 == "-":
    print(ftest11 - ftest12)
elif ftest0 == "*":
    print(ftest11 * ftest12)
else:
    print(ftest11 / ftest12)
