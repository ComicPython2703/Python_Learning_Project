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
list1 = ["上海", "北京", "江苏", "浙江"]
str1 = tk.StringVar()  # 动态变量
label1 = tk.Label(root, bg="gray", width=20, height=3, textvariable=str1)


# ==========={创建函数}=============
def click():
    value = listbox1.get(listbox1.curselection())
    str1.set(value)


# ==========={主程序}==================
# noinspection PyTypeChecker
listbox1 = tk.Listbox(root, listvariable=0)
listbox1.insert("0", "新疆")
listbox1.insert("end", "青岛")
# 插入 = insert
for i in list1:
    listbox1.insert("end", i)
button1 = tk.Button(root, text="Choose", bg="SkyBlue", command=click)
label1.pack()
listbox1.pack()
button1.pack()
# —————————————————————————————
root.mainloop()
lesson("Python")
