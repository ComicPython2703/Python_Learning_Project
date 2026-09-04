# coding=utf-8
import turtle
t=turtle.Turtle()

t.speed(0)

t.pu()
t.goto(0,-200)
t.pd()
t.circle(200)
# 圆一
t.penup()
t.goto(-100,50)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.circle(20)
t.end_fill()
# 圆二
t.penup()
t.goto(100,50)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
# 鼻子
t.penup()
t.goto(0,50)
t.pendown()
# t.circle(-50,,)
t.right(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
# 嘴巴
t.penup()
t.goto(-150,-70)
t.pendown()

t.forward(-100)
turtle.done()
