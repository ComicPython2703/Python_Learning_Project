# coding=utf-8
import turtle

t = turtle.Turtle()

t.speed(0)  # t.速度(最快)
c = ["red", "yellow", "blue", "cyan", "orange", "purple", "pink"]  #c=[红,黄,蓝,青,橘,紫,粉]
t.width(20)  #
r = 180  #
for i in c:  #
    t.pu()  #
    t.goto(0, -r)  #
    t.pd()  #
    t.color(i)  #
    t.circle(r)  #
    r -= 25  #
