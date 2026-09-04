# coding=utf-8
def function(lesson16):
    print(f"Hi,{lesson16}")


def num(x):
    if x == 1:  # 结束条件
        return 1
    else:
        return x + num(x - 1)  # 递归关系


if __name__ == '__main__':
    print(num(5))


def rabbit(n):
    if n <= 2:
        return 1
    else:
        return rabbit(n - 1) + rabbit(n - 2)


if __name__ == '__main__':
    print(rabbit(3))
