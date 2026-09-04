# coding=utf-8
# encoding=utf-8
if __name__ == '__main__':
    print("====================== RESTART:计算器.py =====================")
    print("已连接到 pydev 调试器(内部版本号 243.23654.177)")


# noinspection PyPep8Naming
def Copyright():
    print("\nCopyright (c) 2010-2025 ComicPython6045 Company & Education.\nAll Rights Reserved.\n")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
# ==========={准备工作}==================
import turtle
t = turtle.Turtle()
# 基础设置
t.width(5)
t.hideturtle()

t.goto(-200,100)
t.goto(0,0)
t.goto(200,100)
t.goto(-200,100)
t.setheading(270)

t.forward(200)
t.left(90)
t.forward(400)
t.left(90)
t.forward(200)

turtle.done()
