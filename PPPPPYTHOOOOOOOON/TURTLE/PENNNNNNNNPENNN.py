# coding=utf-8
import turtle

t = turtle.Turtle()
colors = ["red", "yellow", "blue"]
t.speed(0)
name = input("Write Your name:")
numbers = int(input("次数:"))
for i in range(numbers):
    t.color(colors[i % 3])
    # noinspection PyTypeChecker
    t.write(name, font=("Microsoft YaHei UI", 16))
    t.left(122)
    t.penup()
    t.forward(i * 2)
    t.pd()

turtle.done()
