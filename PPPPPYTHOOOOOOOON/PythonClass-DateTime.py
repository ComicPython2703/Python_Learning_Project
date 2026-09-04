# coding=utf-8
import datetime
import random
import turtle

#------------------------------------------------
#  Copyright (c) 2010-2025 ComicPython6045. All Rights Reserved
#------------------------------------------------

class DateTimeClock:
    def __init__(self):
        self.setup_turtle()
        
    def setup_turtle(self):
        turtle.tracer(0)
        self.t = turtle.Turtle()
        self.t2 = turtle.Turtle(visible=False)
        self.t3 = turtle.Turtle()
        self.t3.speed(0)
        self.t.speed(0)
        self.t2.speed(0)
        self.draw_background()
        
    def draw_background(self):
        self.t2.pu()
        self.t2.goto(0, -240)
        self.t2.pd()
        self.t2.circle(250)
        
        for i in range(100):
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            c = random.random()
            c1 = random.random()
            c2 = random.random()
            self.t3.pu()
            self.t3.goto(x, y)
            self.t3.pd()
            self.t3.color(c, c1, c2)
            self.t3.circle(20)
    
    def get_weekday(self, now):
        week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        wd = now.weekday()
        return week[wd]
    
    def get_time(self, now):
        h = now.hour
        m = now.minute
        s = now.second
        return f'{h:02d}时{m:02d}分{s:02d}秒'
    
    def get_date(self, now):
        y = now.year
        m = now.month
        d = now.day
        return f'{y}年{m}月{d}日'
    
    def tick(self):
        now = datetime.datetime.now()
        self.t.clear()
        self.t.write(self.get_date(now) + self.get_weekday(now), 
                    align='center', font=('微软雅黑', 30, "bold"))
        self.t.pu()
        self.t.goto(0, -100)
        self.t.write(self.get_time(now), 
                    align='center', font=('微软雅黑', 30, "bold"))
        self.t.goto(0, 0)
        turtle.ontimer(self.tick, 1000)

if __name__ == '__main__':
    clock = DateTimeClock()
    clock.tick()
    turtle.done()