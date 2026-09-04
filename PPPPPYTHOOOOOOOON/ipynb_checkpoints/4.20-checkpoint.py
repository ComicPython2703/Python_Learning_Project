# coding=utf-8
# 第一个内容


dicts = {
    "语文": 99,
    "数学": 100,
    "英语": 99
}
print("考试结束,成绩如下")
print(dicts.items())
print("科目")
print(dicts.keys())
print("成绩")
print(dicts.values())
# 第二个内容
# 添加
print("发现新科目")
dicts["科学"] = 60
print('dicts["科学"] = 60')
print("现成绩如下")
print(dicts.items())
#
dicts2 = {
    "物理": 70,
    "英语": 1145
}
print("请不要离开，检测到有成绩变更.........")
print("ALL DONE")
dicts.update(dicts2)
print("成绩：", dicts.items())
# 删除
a = dicts.pop(input("要作废那个成绩："))
print("[Server input.output]删除了", a)
print("成绩：", dicts.items())
dicts.clear()
print("[WARING]<class 'dicts'>字典被删除")
# 作业
phones = {
    "啸冥": 114514,
    "啸烘": 54188,
    "啸锭腚": 422,
    "啸桥": 437
}
while True:
    print("当前颠话本如下：")
    print(phones.items())
    b = input("你要茬找谁? ：")
    if b in phones:
        print("裆钱颠话：", phones.get(b))
    else:
        print(f"[ERROR]无法茬到{b},请录入")
        phones[input("你要加入谁：")] = int(input("颠话："))
        print(phones.items())
    c = input("屎否鸡许y :")
    if c == 1:
        pass
    else:
        break
