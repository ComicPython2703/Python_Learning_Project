# coding=utf-8
import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red", "yellow", "blue", "green"]

for i in range(100):
    t.color(colors[i % 3])
    t.forward(i * 2)
    t.left(122)

turtle.done()
