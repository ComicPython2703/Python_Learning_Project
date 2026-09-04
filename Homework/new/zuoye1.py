# coding=utf-8
# 第一个作业
s = 0
for i in range(5, 501, 5):
    s += i
print(s)
# 第二个作业
list2 = []
for x in range(1, 259):
    if 256 % x == 0 and 668 % x == 0:
        list2.append(x)
print("256和668的公因数是：", list2)
print("256和668的最大公因数是：", max(list2))
