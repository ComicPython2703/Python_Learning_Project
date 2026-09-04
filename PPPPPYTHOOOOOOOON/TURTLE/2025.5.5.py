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
# 跑到天崩开局
t.penup()
t.goto(50, 100)
t.pendown()
print("[跑到天崩开局]完成!")
# 设置宽度
t.width(10)
print("[设置宽度]完成!")
# 划红线
t.color('red')
t.setheading(270)
t.forward(200)
print("[划红线]完成!")
# 划蓝线
t.penup()
t.goto(50, 100)
t.pendown()
t.color('blue')
t.setheading(360)
t.circle(-100,180)
print("[划蓝线]完成!")
turtle.done()
