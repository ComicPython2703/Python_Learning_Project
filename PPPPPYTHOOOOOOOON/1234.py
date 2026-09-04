# coding=utf-8
from random import *
file = open("加法.txt", "a+")
for i in range(95):
    a = randint(1, 10)
    b = randint(1, 10)
    s = f"{a}+{b}=\n"
    file.write(s)
file.seek(0, 0)
info = file.read()
print(info)
file.close()
