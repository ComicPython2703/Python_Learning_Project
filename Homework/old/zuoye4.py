# coding=utf-8
import random
import turtle
import time

t = turtle.Turtle()
for i in range(3, 0, -1):
    a = random.random()
    b = random.random()
    c = random.random()
    t.color(a, b, c)
    t.write(i, align="center", font=("", 200, ""))
    time.sleep(1)
    t.clear()
t.write("好?好?学习", align="center", font=("", 100, ""))
t.speed(0)
c = ["yellow", "green", "blue", "red", "pink", "cyan"]
for j in range(50):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(c[j % 6])
    t.circle(10)

turtle.done()
