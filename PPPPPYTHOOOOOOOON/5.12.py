# coding=utf-8
# 第一个内容
print("已连接到 py dev 调试器(内部版本号 223.8836.43)")
list1 = []
for x in range(1, 259):
    if 258 % x == 0:
        list1.append(x)
if __name__ == '__main__':
    print("258的公因数是：", list1)
# 第二个内容
list2 = []
for x in range(1, 259):
    if 256 % x == 0 and 368 % x == 0:
        list2.append(x)
print("256和368的公因数是：", list2)
print("256和368的最大公因数是：", max(list2))
# 第三个内容
list3 = []
for i in range(1, 100):
    sum1 = 0
    for j in range(1, i):
        if i % j == 0:
            sum1 += j
    if sum1 == i:
        list3.append(i)
print(list3)
# 第四个内容
for i in range(2020, 3000):
    a = i // 1000  # 千位数字
    b = i % 1000 // 100  # 百位数字
    c = i % 1000 % 100 // 10  # 十位数字
    d = i % 10  # 个位数字
    if a == d and b == c:
        print(i)
# 方法二
for i in range(2020, 3000):
    i = str(i)
    a = i[3]
    b = i[2]
    c = i[1]
    d = i[0]
    if a == d and b == c:
        print(i)
# 第四个内容
s = 0
for i in range(1, 100, 2):
    s += i
print("1+3+5+7+9+.....+99的和为：", s)
