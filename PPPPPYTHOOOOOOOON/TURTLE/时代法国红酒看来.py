# coding=utf-8
import turtle

t = turtle.Turtle(visible=False)
t.speed(0)
# 鼻子
t.color("red")
t.penup()
t.goto(-50, 0)
t.right(90)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
# 左眼
t.penup()
t.goto(-100, 0)
t.pendown()
t.left(-180)
t.color("gray")
t.begin_fill()
for i in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()
t.color("black")
t.goto(-50, 0)
t.begin_fill()
for i in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()
# 右眼
t.penup()
t.goto(150, 0)
t.pendown()
t.color("gray")
t.begin_fill()
for i in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()
t.color("black")
t.goto(100, 0)
t.begin_fill()
for i in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()
turtle.done()
print("THE END")
