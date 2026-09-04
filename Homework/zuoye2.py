# coding=utf-8
a1 = int(input("年："))
a2 = int(input("🈷："))
a3 = int(input("囸："))
mom = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (a1 % 4 == 0 and a1 % 100 != 0) or a1 % 400 == 0:
    mom[1] = 29
count = sum(mom[:a2 - 1]) + a3
print(count)
