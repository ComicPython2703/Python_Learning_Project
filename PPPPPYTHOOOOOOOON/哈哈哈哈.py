# coding=utf-8
print("Debug started")
# 第一个内容
mum = 114514
apple = 541.88
# 第一种做法
print(f"买了{mum}斤🍎,每斤{apple}money")
#     f=float 小数点
# 第二种做法
print("买了%d斤🍎,每斤%.2f元" % (mum, apple))
#           %d=整数        %2f=只保留2位小数
# 第三种做法
print("买了{0}斤🍎,每斤{1}money".format(mum, apple))
#         {0}=mum 也就是第1个 {1}同理
# 第二个内容
import time
work = ["扫地", "拖地", "洗碗", "洗衣服"]
for i in work:
    print(f"🐎:给我干家务！{i}")
    time.sleep(1)
    if i == "洗碗":
        print("小明:我不干了,你个傻逼!🤬🤬🤬")
        print("[WARNING]小明已被🐎使用”他叫剑“杀死了")
        print("[INFO]小明已复活")
        continue
    else:
        print(f"小明:{i}好了😉")
# 第三个内容
import random
print("//////////////士兵与强盗\\\\\\\\\\\\\\\\\\\\\\\\\\")
shibing = 5  # a
qiangdao = 10  # b
lunshu = 1  # i
try:
    while shibing > 0:
        print("round%d" % lunshu)
        print("士兵:妈的你这个sb给我投降,俺楚某保证你的生命安全！")
        print("强盗:楚某,我日你仙人! 放下武器交出宝藏!")
        lunshu += 1
        c = random.randint(1, 3)
        print("[Debug]number is:%d" % c)
        guess = int(input("输入1-3之间的数字以解决冲突："))
        if guess == c:
            qiangdao -= c
            print("😎,你猜对了！ 强盗死了%d个" % c)
        else:
            shibing -= 1
            print("😨,wc你猜错了,死了1个士兵,剩%d个士兵" % shibing)
        if qiangdao < 5:
            print("[WARNING]强盗被士兵使用“命运”杀死了")
            print("士兵:哈哈哈哈哈哈哈哈哈🤣🤣😂,你,菜就多练,输不起,就别玩")
            print("[INFO]士兵已胜利!")
            print("士兵还剩%d" % shibing)
            break
    else:
        print("[WARNING]士兵被强盗使用“命运”杀死了")
        print("强盗:哈哈哈哈哈哈哈哈哈🤣🤣😂,你,菜就多练,输不起,就别玩")
        print("强盗:哈哈哈,宝藏是俺们的了！")
except ValueError:
    print("[ERROR]输入的类型错误! 请重新输入！")