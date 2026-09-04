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
    print("\n已连接到 pydev 调试器(内部版本号 241.17011.127)\n")

# ==================================
# #########{创建函数;类}#####################
class Car:
    car_brand = "BYD"

    def __init__(self, name, year, model):  # #{{{构造方法}}}##
        self.name = name  # 实例属性  每个对象相互独立,互不影响
        self.model = model
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

    def __price(self):
        if self.model == 'tang':
            self.price = 21
        elif self.model == 'song':
            self.price = 40
        else:
            self.price = 100
        self.tax = self.price * 0.1
        total = self.price + self.tax
        return total

    def money(self):
        print(self.__price())


# ########{诸城市}#############
car1 = Car("BYD", 2022, 'tang')
car1.money()
