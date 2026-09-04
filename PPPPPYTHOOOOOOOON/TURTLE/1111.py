# coding=utf-8
import turtle
t = turtle.Turtle()

t.speed(0)
t.width(3)

t.color("red")
t.circle(100)
t.color("blue")
t.left(30)
for i in range(6):
    t.forward(100)
    t.left(60)
turtle.done()
