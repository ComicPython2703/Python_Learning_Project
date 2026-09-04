# coding=utf-8
# encoding=utf-8
# 不要看这里!!!!

if __name__ == '__main__':
    print("====================== RESTART:计算器.py =====================")
    print("已连接到 pydev 调试器(内部版本号 243.23654.177)")


# 不要看这里!!!!


# noinspection PyPep8Naming
def Copyright():
    print("\nCopyright (c) 2010-2025 ComicPython6045 Company & Education.\nAll Rights Reserved.\n")


# 不要看这里!!!!


def lesson(python):
    print(f'Hi,{python}')


# 不要看这里!!!!


if __name__ == '__main__':
    Copyright()

# ==========={准备工作}==================
import turtle

t = turtle.Turtle()
# 设置宽高速度
t.speed(0)
t.width(5)
t.speed(0)
# 去往底下
t.penup()
t.goto(0, -200)
t.pd()
# 200半径圆
t.circle(200)
# 覆盖颜色(黑色)
t.fillcolor("black")
# 开始覆盖
t.begin_fill()
t.circle(100, -180)
t.circle(-100, -180)
t.circle(-200, -180)
t.end_fill()
# 停止覆盖
t.right(90)
t.color("black")
t.penup()
t.forward(100)
t.dot(50)
t.color("white")
t.forward(200)
t.dot(50)

turtle.done()
