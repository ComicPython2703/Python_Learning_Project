# coding=utf-8
# encoding=utf-8
# W269N-WFGWX-YVC9B-4J6C9-T83GX
# irm https://get.activated.win | iex


if __name__ == '__main__':
    print("====================== RESTART:登录界面.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


def Copyright():
    print("\nCopyright (c) 2010-2024 ComicPython6045 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print()
# ==========={准备工作}==================
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Program for file=[12.8（登录界面）.py]")
names = {"XiaoShuai": "asas12345678",
         "LaoZhang": "aaassqwwe24",
         "Example": "example",
         }


# ==========={创建函数}==================、
def login():
    val1 = entry1.get()
    val2 = entry2.get()
    if val1 in names:
        if val2 == names[val1]:  # 字典通过key值判断value
            messagebox.showinfo("Hello", "登录成功")
        else:
            messagebox.showinfo("ERROR", "Password Error")
    else:
        messagebox.showinfo("ERROR", "账号不存在")


def register():
    val1 = entry1.get()
    val2 = entry2.get()
    names[val1] = val2
    messagebox.showinfo("Success", "成功注册")
    entry2.delete("0", "end")
    entry1.delete("0", "end")


# ==========={主程序}==================
# 标签组件
label1 = tk.Label(root, text="账号：")
label1.grid(row=0, column=0)  # row=行 , column=列
label2 = tk.Label(root, text="密码：")
label2.grid(row=1, column=0)
# 文本框
entry1 = tk.Entry(root)
entry1.grid(row=0, column=2, padx=11, pady=6)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=2, pady=6)
# 按钮
button1 = tk.Button(root, text="Login", width=4, height=1, bg='SkyBlue', command=login)
button1.grid(row=2, column=0)
button2 = tk.Button(root, text="register", width=6, height=1, bg='yellow', command=register)
button2.grid(row=2, column=2, sticky="e")
# entry = 单行
# text = 多行
lesson("Python")
root.mainloop()
