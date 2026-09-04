# coding=utf-8
import turtle

t = turtle.Turtle()
t.color("red")
t.circle(90, 90)
t.color("yellow")
t.circle(90, 90)
t.color("blue")
t.circle(90, 90)
t.color("orange")
t.circle(90, 90)
t.left(90)
t.forward(180)

r = 30
for i in range(30, 150, 30):
    t.circle(i, 180)

turtle.done()
