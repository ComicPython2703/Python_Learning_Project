# coding=utf-8
# encoding=utf-8
"""
Title= 图形化设计-part-1
"""
if __name__ == '__main__':
    print("====================== RESTART:图形化设计-part-1.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


def Copyright():
    print("\nCopyright (c) 2010-2024 ComicPython6405 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print()

# =========={准备工作}==================
import tkinter as tk
root = tk.Tk()
root.title("Program for file=[12.1（图形化设计）.py]")
root.geometry('700x600')
sstr = tk.StringVar()
label1 = tk.Label(root, bg="LightBlue", textvariable=sstr, font=("Microsoft JhengHei Ui", 23), width=20, height=4)
click = 0
click2 = 0
entry1 = tk.Entry(root)  # 单行
entry1.pack()


# ============{创建函数}=================
def launch1():
    label1.pack()


def on_click():
    global click  # 声明为全局变量
    if click == 0:
        sstr.set("你好:)")
        click = 1
    else:
        sstr.set("nihao:)")
        click = 0


# entry = 单行
# text = 多行

def on_click_two():
    global click2  # 声明为全局变量
    if click2 == 0:
        sstr.set("oi,小鬼,今天看起来很火热啊")
        click2 = 1
    else:
        sstr.set("OOOOOIIIIIIIIIIII:)")
        click2 = 0


def password():
    val = entry1.get()
    if val == "123456":
        text1.insert("insert", "密码正确")
    else:
        text1.insert("insert", "密码错误")


# ============={主程序}==================
if __name__ == '__main__':
    button1 = tk.Button(root, bg="green", text="启动标签🏷", font=("Microsoft JhengHei Ui", 23), width=15, height=4,
                        command=launch1)
    button2 = tk.Button(root, bg="blue", text="启动字符1", font=("Microsoft JhengHei Ui", 23), width=15, height=4,
                        command=on_click)
    button3 = tk.Button(root, bg="red", text="启动字符二", font=("Microsoft JhengHei Ui", 23), width=15, height=4,
                        command=on_click_two)
    button1.pack(side=tk.LEFT)
    button2.pack(side=tk.RIGHT)
    button3.pack()
    entry1 = tk.Entry(root)
    entry1.pack()
    text1 = tk.Text(root, height=2)
    text1.pack()
    button4 = tk.Button(root, text="尝试登录", font=("Microsoft JhengHei Ui", 23), width=6, height=1, command=password)
    button4.pack()
    root.mainloop()
    lesson("Python")
