# coding=utf-8
import turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("pink")
for i in range(4):
    t.forward(100)
    t.right(90)
t.setheading(-90)
for i in range(4):
    t.forward(100)
    t.right(90)
t.setheading(90)
for i in range(4):
    t.forward(100)
    t.right(90)

for i in range(4):
    t.forward(100)
    t.right(-90)
turtle.done()
