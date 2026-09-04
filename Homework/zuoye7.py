# coding=utf-8
n = int(input("输入数字<n>："))
k = int(input("输入数字<k>："))
s1, s2 = 0, 0


def zuoye1():
    global s2, s1
    for i in range(1, n + 1):
        if i % k == 0:
            s1 = s1 + i
        else:
            s2 = s2 + i
    print("s1-s2的值：", abs(s1 - s2))


if __name__ == '__main__':
    zuoye1()
