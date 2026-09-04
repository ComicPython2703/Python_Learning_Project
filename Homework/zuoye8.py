# coding=utf-8
# =========={准备工作}==================
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("zouye8")
root.geometry('300x150')


def say_ni():
    messagebox.showinfo("启动1", "WOWEE")


def say_hi():
    messagebox.showinfo("启动2", "I'm GOOD")


def say_hhi():
    messagebox.showinfo("启动3", "I'm SO CLEVER!")


# ============{创建函数}=================

button1 = tk.Button(root, text="启动1", width=25, height=2, bg='SkyBlue', command=say_ni)
button2 = tk.Button(root, text="启动2", width=25, height=2, bg='Firebrick1', command=say_hi)
button3 = tk.Button(root, text="启动3", width=25, height=2, bg='Wheat1', command=say_hhi)
button1.pack()
button2.pack()
button3.pack()

root.mainloop()
