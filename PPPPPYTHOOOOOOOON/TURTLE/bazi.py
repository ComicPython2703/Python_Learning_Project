# coding=utf-8
import turtle

t = turtle.Turtle()

t.speed(0)
c = ["white", "white", "black", "black", "blue", "blue", "red", "red", "yellow", "yellow"]
r = 200
for i in c:
    t.pu()
    t.goto(0, -r)
    t.pd()
    t.color("black", i)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    r -= 20
t.penup()
t.goto(0, -140)
t.pd()
t.color("white")
t.circle(140)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
t.color("pink")
x = -190
for i in n:
    t.pu()
    t.goto(x, -8)
    t.pd()
    t.write(i)
    if i == 10:
        x += 15
    x += 20
