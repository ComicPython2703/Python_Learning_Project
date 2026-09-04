# coding=utf-8
import turtle
from turtle import Turtle

t: Turtle = turtle.Turtle()
t.speed(0)
c = ["cyan", "blue", "orange", "yellow", "red", "pink"]
t.width(4)
for i in range(6):
    t.color(c[i % 6])
    t.circle(100, 360, 6)
    t.left(360 / 6)

turtle.done()
