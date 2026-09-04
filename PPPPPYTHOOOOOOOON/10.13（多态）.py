# coding=utf-8
"""
Title=多态
"""
if __name__ == '__main__':
    print("====================== RESTART:多态.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


# noinspection PyPep8Naming
def Copyright():
    print("\nCopyright (c) 2010-2024 ComicPython6405 Foundation.\nAll Rights Reserved.")


# noinspection PyShadowingNames
def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print()

# =========={准备工作}==================
import tkinter as python

root = python.Tk()
python.Label(root, text="Python").grid(row=1)


# ============{分隔符}==================
# ###############{创建函数或类}###################
# noinspection PyPep8Naming
class Animals:  # 父类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print(f'{self.name}今年{self.age}岁')


class Person(Animals):
    def sayHello(self):
        print(f'{self.name}今年{self.age}岁')


class Dog(Animals):
    def sayHello(self):
        print(f'{self.name}今年{self.age}岁')


# =========={诸城市}=================
animal = Animals("Animalistically", 15)
person = Person("tom", 36)
dog = Dog("digraph", age=4)
animal.sayHello()
person.sayHello()
dog.sayHello()

root.mainloop()
