# coding=utf-8
print("PyDev console: starting.")
# 第一个问题
up = 2
down = 1
dist = 0
day = 0
while True:
    day += 1
    dist += up
    print(f"过去了{day}🕖天,🐌爬了{dist}米")
    if dist >= 10:
        print("")
        break
    dist -= down
print("爬了", day, "天")
# 第二个问题
a = 0
for i in range(4):
    a = (a + 6) / 2
print(f"李白酒瓶🎁原有{a}升酒")
# 第三个问题
money = 20
n = money
while n >= 3:
    b = n // 3
    c = n % 3
    money = money + b
    n = a + b

if n == 2:
    money += 1
