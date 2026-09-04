# coding=utf-8
import turtle

t = turtle.Turtle()

t.color("pink")
t.forward(123)
t.color("red")
t.left(120)
t.color("yellow")
t.forward(123)
t.color("blue")
t.left(120)
t.color("green")
t.forward(123)
for i in range(5):
    t.color("pink")
    t.left(360 / 5)
    t.forward(200)

for i in range(6):
    t.color("orange")
    t.left(360 / 6)
    t.forward(200)

for i in range(7):
    t.color("red")
    t.left(360 / 7)
    t.forward(200)

for i in range(8):
    t.color("blue")
    t.left(360 / 8)
    t.forward(200)

for i in range(9):
    t.color("yellow")
    t.left(360 / 9)
    t.forward(200)
