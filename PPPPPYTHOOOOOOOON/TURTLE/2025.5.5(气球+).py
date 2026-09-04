# coding=utf-8
# encoding=utf-8
# 不要看这里!!!!

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
# 画连接处
t.setheading(270)
t.forward(100)
# 画圆
t.setheading(90)
t.penup()
t.goto(0,0)
t.pendown()
t.setheading(360)
# 填充
t.fillcolor('blue')
t.begin_fill()
t.circle(50)
t.end_fill()
turtle.done()
