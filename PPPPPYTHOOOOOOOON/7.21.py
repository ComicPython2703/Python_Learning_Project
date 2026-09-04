# coding=utf-8
# ======write.time----
# ======<local.time>-7.21


def pythonlesson(model):
    print(f"hi,{model}")


import calendar
import fractions
import time

t0 = time.localtime()
t1 = time.asctime()
if __name__ == '__main__':
    print(time.time())
    print('当前时间：', t0)
    print(t0[8])
    print('🗓现在是📆⏱⏰⏲：{Time:', t1, '}')
    # time.sleep(1) 等待一秒
    c0 = calendar.month(2024, 7)
    # noinspection PyNoneFunctionAssignment
    c1 = calendar.prcal(2024)
    if __name__ == '__main__':
        print(c0)
        print(c1)
    c1145 = int(input("请输入年："))
    print("你输入的年为：", calendar.isleap(c1145))
    f1 = fractions.Fraction(4, 7)
    # 变量名=分数.分数(分子,分母)
    f2 = fractions.Fraction(114, 514)
    print(f1 + f2)
    print(f1 * f2)
    print(f1 / f2)
    print(f1 - f2)
# _____________----------------_____________---------#
# ===========分割线===============#
