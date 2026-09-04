# coding=utf-8
import turtle

t = turtle.Turtle()
n = int(input("请输入边数"))

for i in range(n):
    t.forward(123)
    t.left(360 / n)
