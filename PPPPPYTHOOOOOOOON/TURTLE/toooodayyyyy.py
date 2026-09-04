# coding=utf-8
import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("purple")
t.penup()
t.goto(-200, 0)
t.pendown()
t.hideturtle()
t.width(20)
n = turtle.textinput("输入长度", "2～8之间")
for i in range(int(n)):
    t.setheading(-40)
    t.color("red")
    t.circle(30, 80)
    t.color("blue")
    t.circle(-30, 80)
t.dot(10, "black")
turtle.done()
