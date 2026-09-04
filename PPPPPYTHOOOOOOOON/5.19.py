# coding=utf-8
# 第一个内容
print("第一个内容")
for i in range(10, 100):
    a = i // 10  # 对10取整
    b = i % 10  # 对10取余
    if (a + b) + (a * b) == i:
        print(i)
# 第二个内容
print("第二个内容")
list1 = []
for i in range(10, 100):
    s = str(i)
    c = int(s[0])
    d = int(s[1])
    if (c + d) + (c * d) == i:
        list1.append(i)
print(list1)
# 第三个内容
print("第三个内容")
print("同构树有：")
print("{")
for i in range(10001):
    res = str(i ** 2)
    s = str(i)
    l = len(s)
    if res[-l:] == s:
        print(i)
print("             }")
# 第四个内容
print("第四个内容")
print("(1)")
for i in range(100, 1000):
    a = i // 100
    b = i % 100 // 10
    c = i % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
print("(2)")
for i in range(100, 1000):
    s = str(i)
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
# 第五个内容
print("第五个内容")
for i in range(1000, 10000):
    s = str(i)
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])
    if a ** 4 + b ** 4 + c ** 4 + d ** 4 == i:
        print(i)
