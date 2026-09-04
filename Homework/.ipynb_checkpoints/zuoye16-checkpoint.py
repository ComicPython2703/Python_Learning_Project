# coding=utf-8
dicts = {
    'k1': 'y1',
    'k2': 'y2',
    'k3': 'y3'
}
print("[System]正在往<class 'dicts'>添加{'k4':'y4'}")
dicts["k4"] = 'y4'
print("Done")
print("当前字典：", dicts.items())
print("[System]正在往<class 'dicts'>删除{'k1':'y1'}")
del dicts['k1']
print("Done")
print("当前字典：", dicts.items())
