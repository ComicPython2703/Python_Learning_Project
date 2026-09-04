# coding=utf-8
print("已连接到 pydev 调试器(内部版本号 231.8109.197)")
# 第一个内容
lest = ["苹果🍎", "芒果", "香蕉🍌"]
for i in lest:
    print("I like %s" % i)
# 第二个内容
a = "ppppppyttttthooooon"
for i in a:
    print(i)
# 第三个内容
b = [1, 2, 3, 4, 5]
for i in b:
    print(i, "*5=", i * 5)
# 第三个内容
for i in range(1, 11, 2):
    print(i)
for i in range(11):
    if i % 2 != 0:
        print(i)
# 第四个内容
for i in range(1, 9):
    for j in range(1, i + 1):
        print("*", end="  ")
    print("")
# 第五个内容
for i in range(1, 11):
    for j in range(1, i + 1):
        print("{0}*{1}={2}".format(j, i, j * i), end="  ")
    print("")
# 第六个内容
for i in range(2, 200):
    for n in range(2, i - 1):
        if i % n == 0:
            break
    else:
        print(i, end="  ")
range(1, 8)
