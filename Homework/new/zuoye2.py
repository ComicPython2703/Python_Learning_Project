# coding=utf-8
for i in range(10000, 1000000):
    s = str(i)
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])
    e = int(s[4])
    if a ** 5 + b ** 5 + c ** 5 + d ** 5 + e ** 5 == i:
        print(i)

for i in range(1000000, 100000000):
    s = str(i)
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])
    e = int(s[4])
    f = int(s[5])
    g = int(s[6])
    if a ** 7 + b ** 7 + c ** 7 + d ** 7 + e ** 7 + f ** 7 + g ** 7 == i:
        print(i)
