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

# =====================================================
import turtle
t=turtle.Turtle()
# ============================================
# 红色园1
t.color("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-50,0)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(50,0)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.pu()
t.goto(-100,-100)
t.pd()

t.color("black")
for i in range(4):
    t.forward(200)
    t.left(90)

turtle.done()



