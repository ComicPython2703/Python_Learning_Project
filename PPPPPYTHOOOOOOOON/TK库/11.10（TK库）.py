# coding=utf-8
# encoding=utf-8
"""
Title= TK库
"""
if __name__ == '__main__':
    print("====================== RESTART:TK库.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


# noinspection PyPep8Naming
def Copyright():
    print("\nCopyright (c) 2010-2024 ComicPython6405 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print()

# =========={准备工作}==================
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Program for file=[11.10（TK库）]")
root.geometry('700x600')


# ============{创建函数}=================
def say_ni():
    print("亻尓女马")


def say_hi():
    messagebox.showinfo("nihao", "woshi")


# ==========={诸城市}=================
button1 = tk.Button(root, text="TEST", width=25, height=2, bg='SkyBlue', command=say_ni)
button2 = tk.Button(root, text="TEST2", width=25, height=2, bg='Firebrick1', command=say_hi)
button1.pack(side=tk.LEFT)
button2.pack(side=tk.RIGHT)
root.mainloop()
