# coding=utf-8
import random
import turtle

t = turtle.Turtle(visible=False)
turtle.bgcolor("black")
for i in range(100):
    a = random.random()
    b = random.random()
    c = random.random()
    t.color(a, b, c)
    t.dot(100)
turtle.done()
