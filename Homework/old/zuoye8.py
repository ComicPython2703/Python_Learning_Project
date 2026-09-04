# coding=utf-8
gender = input("性别:")
age = int(input("年龄:"))
if gender == "f":
    if 10 <= age <= 12:
        print("可以参加")
else:
    print("不可参加")
