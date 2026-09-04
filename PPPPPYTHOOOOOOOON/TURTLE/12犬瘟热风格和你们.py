# coding=utf-8
import turtle
import random
t = turtle.Turtle()
t.speed(0)
c1 = ["yellow", "green", "blue", "red", "pink", "cyan"]
c2 = random.sample(c1, 4)
print(c2)
for i in range(4):
    t.color(c2[i])
    for j in range(4):
        t.forward(100)
        t.left(90)
    t.right(90)

turtle.done()
