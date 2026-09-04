# coding=utf-8
"""

Title=类与对象
"""


# noinspection PyPep8Naming
def Copyright():
    print(
        "\nCopyright (c) 2018-2024 Luxue Education .\nAll Rights Reserved.\n\nCopyright (c) 2010-2024 ComicPython6405 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print()
# ############{准备工作}######################
""" 面向对象是编程的一种思想,按照真实世界的思维方式去构建软件系统"""


# #############{分隔符}######################
# ==========={创建函数或类}===================
class Car:
    print("都有IV个轮子")
    print('都优罚洞鸡')
    time = 2022

    @staticmethod
    def brand(name):  #类的对象
        print()
        print(f'这是{name}牌车')
        print('它有T4级别阀侗只因')


class Doooggg:  #类
    def __init__(self, name, age):  #构造方法
        self.name = name  #实例变量
        self.age = age

    def eat_shi(self):  #类方法
        print()
        print(f'{self.name},你可以吃芝士汉堡')


# #############{分隔符}###################### ==========={诸臣是}=================
car = Car()
car.brand('BYD')
dog = Doooggg("小猫", 114514)
dog.eat_shi()
