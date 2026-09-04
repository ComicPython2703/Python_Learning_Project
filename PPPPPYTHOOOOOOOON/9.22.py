# coding=utf-8
"""
Title=类的继承
"""
if __name__ == '__main__':
    print('正在运行程式：D:\Python38\python.exe -X pycache_prefix=C:/users\EDY\AppData\Local\JetBrains\PyCharmCE2024.1\cpython'
          '-cache "C:/Program Files/JetBrains/PyCharm Community Edition '
          '2024.1.2/plugins/python-ce/helpers/pydev/pydevd.py" --multiprocess --qt-support=auto --client 127.0.0.1 '
          '--port 51222 --file E:\Python\PPPPPYTHOOOOOOOON\9.22.py ')
    print("====================== RESTART:继承.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


def Copyright():
    print("\nCopyright (c) 2010-2024 ComicPython6405 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print()


# =========={准备工作}==================

# ============{分隔符}==================
# ###############{创建函数或类}###################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_Hello(self):
        print(f'全民制作人们大家好,我是练习时长{self.age}年半的{self.name}')


class Student(Person):  # 加了括号，这叫【继承】 Person叫【父类】
    def __init__(self, name, age):
        super().__init__(name, age)
        self.grade = 8

    def say_Hello(self):  # 可有可无，重写【父类】方法
        print(f"亻尔女子,我是练习时长{self.age}年半的{self.name},上早{self.grade}")


# =========={诸城市}=================
st1 = Person("蔡徐坤", 2)
st2 = Student("坤坤", 1145)
st1.say_Hello()
st2.say_Hello()
lesson("Python")
