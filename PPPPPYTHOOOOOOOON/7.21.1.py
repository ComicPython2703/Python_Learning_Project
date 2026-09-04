# coding=utf-8
# coding=utf-8
import datetime

now = datetime.datetime.now()
print("----------------------------------")
print("|", now, "|")
print("----------------------------------")
print()
print(now.year)
print(now.month)
print(now.hour)


def getdate():
    y = now.year
    m = now.month
    d = now.day
    print(y, m, d)


def gettimmmmeeeeee():
    h = now.hour
    m = now.minute
    s = now.second
    print(h, m, s)


