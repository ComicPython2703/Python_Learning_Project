# coding=utf-8
"""
Title= 猜数字+
"""
if __name__ == '__main__':
    print("====================== RESTART:猜数字+.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


# noinspection PyPep8Naming
def Copyright():
    print("\nCopyright (c) 2010-2024 ComicPython6405 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


Copyright()
print()

# =========={准备工作}==================
import random as r

a = r.randint(1, 100)
# ============={创建函数或类}===============
if __name__ == '__main__':
    print("======={猜数字+}=========")
    while True:
        try:
            b = int(input("输入数字："))
            if b == a:
                print("猜对了！🥳")
                print("—————{THE+END}—————")
                break
            elif b > a:
                print("你猜大啦🤯")
            else:
                print("你猜小辣！😱")
        except ValueError:
            print("[ERROR]⛔ValueError: invalid literal for int() with base 10: str")
            print("[WARNING]⚠️发现非<int>值，请重新输入！")
