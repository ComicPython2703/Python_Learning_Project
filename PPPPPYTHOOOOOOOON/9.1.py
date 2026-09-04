# coding=utf-8
"""
Title=类与属性
"""


def Copyright():
    print(
        "\nCopyright (c) 2018-2024 Luxue Education .\nAll Rights Reserved.\n\nCopyright (c) 2010-2024 ComicPython6405 "
        "Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print()


# ====================={准备工作}=================

# ============={创建类}====================
class Car:
    car_brand = input("品牌:")

    def __init__(self, name, year):  # #{{{构造方法}}}##
        self.name = name  # 实例属性  每个对象相互独立,互不影响
        self.year = year  # 实例属性  每个对象相互独立,互不影响
        self.mile = 0  # 设置默认值 不用填写形参

    def get_data(self):  # 类方法
        data = self.car_brand + "-" + self.name + "-" + self.year
        return data

    @staticmethod
    def setup_brand(brand):  # 类方法
        Car.car_brand = brand  # 修改类属性

    def get_mile(self):
        return "Drove:" + str(self.mile)

    def set_mile(self, m):
        self.mile = m


# ###########{诸臣式}######################
car1 = Car('SSR114', '1145')  # CAR1=对象 类名
car2 = Car('h9f48', '2077')
car3 = Car('M1145', '2077')
car3.setup_brand('Tesla')
print(car1.get_data())
print(car2.get_data())
print(car3.get_data())
print(car3.get_mile())
car3.mile = 114514  # 通过实例方法修改属性值
print(car3.get_mile())

lesson(python="Class")
