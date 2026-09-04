# coding=utf-8
def Copyright():
    print("\nCopyright (c) 2010-2025 ComicPython6045 Company & Education.\nAll Rights Reserved.\n")
Copyright()
# =============================================================
import turtle
t=turtle.Turtle()
t.width(5)

# 120半径圆🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣😂😂😂😂😂
t.circle(120)

# 60 半径圆 -180改变开口方向
t.circle(60,-180)

# 再次画圆,左方向60
t.circle(-60,-180)

# 去往(0,40)位置
t.penup()
t.goto(0,40)
t.pendown()

# 画20半径圆
t.circle(20)

# 跑到(0.160) 并画圆
t.penup()
t.goto(0,160)
t.pendown()
t.circle(20)
turtle.done()
