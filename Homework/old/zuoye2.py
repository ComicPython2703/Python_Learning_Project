# coding=utf-8
import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, 0)
t.pd()
for i in range(4):
    t.setheading(-40)
    t.circle(30, 80)
    t.circle(-30, 80)
turtle.done()
