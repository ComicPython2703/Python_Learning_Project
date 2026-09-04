# coding=utf-8
def hanshu(homework):
    print(f'hi{homework}')


# noinspection PyShadowingNames
def f(n):
    if n <= 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


n = int(input("请输入一个正整数,它是<n>："))
if __name__ == '__main__':
    print(f(n))

n = f(n - 1) * 2
