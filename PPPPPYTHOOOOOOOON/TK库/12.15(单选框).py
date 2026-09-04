# coding=utf-8
# encoding=utf-8
if __name__ == '__main__':
    print("====================== RESTART:单选框.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


def Copyright():
    print("\nCopyright (c) 2010-2025 ComicPython6045 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print()
# ==========={准备工作}==================
import tkinter as tk

root = tk.Tk()
root.title("Program for file=[12.15（单选框）.py]")
root.geometry('700x600')
str1 = tk.StringVar()  # 设置文本变量
# noinspection PyTypeChecker
str1.set(0)


# ==========={创建函数}=============
# noinspection PyGlobalUndefined
def select():
    global t
    val = str1.get()
    if val == "A":
        t = "去挖矿去吧！"
    if val == "B":
        t = "你太贪吃了"
    if val == "C":
        t = "一个崩溃你就老实了"
    if val == "D":
        t = "你无敌了"
    text1.delete("1.0", "end")
    text1.insert("insert", t)


"""
增=insert
删=delete
改=update
查=select
 """

# ==========={主程序}==================
# Radiobutton=单选
label1 = tk.Label(root, bg="LightBlue", text="你需要社么？", font=("Microsoft JhengHei Ui", 23), width=15, height=1)
r1 = tk.Radiobutton(root, text="A.钻石镐", variable=str1, value="A", command=select)
r2 = tk.Radiobutton(root, text="B.附魔金苹果", variable=str1, value="B", command=select)
r3 = tk.Radiobutton(root, text="C.Mods", variable=str1, value="C", command=select)
r4 = tk.Radiobutton(root, text="D.下界合金箭", variable=str1, value="D", command=select)
text1 = tk.Text(root, height=2)
label1.pack()
r1.pack()
r2.pack()
r3.pack()
r4.pack()
text1.pack()
# —————————————————————|输入框|—————
lesson("Python")
root.mainloop()
