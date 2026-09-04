# coding=utf-8
copyright()
import turtle
t = turtle.Pen()
t.speed(0)
for i in range(80):
    t.forward(40)
    t.right(-5)
for i in range(80):
    t.forward(40)
    t.right(5)
for x in range(1, 300, 2):
    t.forward(x)
    t.right(90)
