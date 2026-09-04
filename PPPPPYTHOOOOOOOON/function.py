# coding=utf-8
import turtle

t = turtle.Turtle()
t.speed(0)


# 含数gv
def function(lesson):
    print(f'Hi, {lesson}')


def print_hi():
    print(f'我是斯奥税😎')  # 定义函树,有返回值


if __name__ == '__main__':
    print_hi()  # 调用函数


def print_hi2(names):
    print(f'我是{names}')  # 定义函树,有返回值


if __name__ == '__main__':
    print_hi2("扣税国王😎,吸气要扣税😆.....")  # 调用函数


def print_hi3(name):
    return f"I am a {name}"


a = print_hi3("god")
if __name__ == '__main__':
    print(a)
# 练习
xm = [618, 733, 431, 534, 824, 564]
xd = [453, 286, 236, 267, 548, 328]
xh = [785, 645, 139, 496, 279, 698]


def student_score(n):
    s = 0
    for i in n:
        s += i
    print(s)


if __name__ == '__main__':
    student_score(xm)
if __name__ == '__main__':
    student_score(xh)
if __name__ == '__main__':
    student_score(xd)


# 画图
def turtle_print(color, n):
    t.color(color)
    t.begin_fill()
    for i in range(n):
        t.fd(100)
        t.left(360 / n)
    t.end_fill()


turtle_print("green", 6)
if __name__ == '__main__':
    print("[TURTLE.INFO]绘图完成")
turtle.done()
