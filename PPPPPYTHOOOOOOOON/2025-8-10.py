# coding=utf-8
# encoding=utf-8
print("Copyright (c) 2010-2025 ComicPython6045 Communicate.\nAll Rights Reserved.\n")


def lesson(python):
    print(f'Hi,{python}')


# ====================================================================
a, b = 0, 0
for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        a += 1
        if 5 * x + 3 * y + z / 3 == 100:
            b += 1
            print(f"公鸡{x},母鸡{y},小鸡{z}")
print(f"循环次数{a},符合买法{b}")
print(f'{a / 3600}')
# ================================
a = b = c = 0
for i in range(2, 101):
    for j in range(2, i + 1):
        b += 1
        if i % j == 0:
            a += 1
    if a == 2:
        print(f'数字{i}是质数')
        c += 1
    a = 0
print(f'循环{b}次,有{c}个')
print(f'{b / 3600}小时')
