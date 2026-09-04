# coding=utf-8
import turtle

t = turtle.Turtle()
t.speed(0)
t.width(5)
t.color("black", "yellow")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

turtle.done()
