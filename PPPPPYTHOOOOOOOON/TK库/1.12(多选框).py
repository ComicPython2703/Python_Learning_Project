# encoding=utf-8
if __name__ == '__main__':
    print("====================== RESTART:多选框.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


# noinspection PyPep8Naming
def Copyright():
    print("\nCopyright (c) 2010-2025 ComicPython6045 Foundation.\nAll Rights Reserved.\n")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()

# ==========={准备工作}==================
import tkinter as tk

root = tk.Tk()
root.title("Program for file=[1.12(多选框).py]")
label1 = tk.Label(root, text="你要捡什么", font=("Microsoft JhengHei Ui", 23), width=15, height=1)
label1.pack()
vars1 = tk.IntVar()
vars2 = tk.IntVar()
vars3 = tk.IntVar()
str1 = tk.StringVar()
label2 = tk.Label(root, textvariable=str1, font=("Microsoft JhengHei Ui", 15))
label2.pack()
c1 = tk.Checkbutton(root, text="1000$", variable=vars1)
c2 = tk.Checkbutton(root, text="1000¥", variable=vars2)
c3 = tk.Checkbutton(root, text="1000€", variable=vars3)


# =============={创建函数}=====================
def select():
    vals1 = vars1.get()
    vals2 = vars2.get()
    vals3 = vars3.get()
    if vals1 and vals2 and vals3:
        str1.set("贪官,斩了")
    elif vals1 and vals2:
        str1.set("为何不捡欧元")
    elif vals1 and vals3:
        str1.set("不捡人民币属于违法行为,自首去吧")
    elif vals2 and vals3:
        str1.set("为何不捡美刀")
    elif vals1:
        str1.set("咋的,你以为你是大漂亮国的人啊,IMPOSSIBLE!")
    elif vals2:
        str1.set("漂亮")
    elif vals3:
        str1.set("咋的,你以为你是欧洲人啊,不可能!")
    else:
        str1.set("")


# ============{主程式}=======================
button1 = tk.Button(root, text="选择", command=select)
c1.pack()
c2.pack()
c3.pack()
button1.pack()
root.mainloop()
lesson("Python")
