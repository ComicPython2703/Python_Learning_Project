# coding=utf-8
# encoding=utf-8


if __name__ == '__main__':
    print("====================== RESTART:名片制作.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


def Copyright():
    print("\nCopyright (c) 2010-2025 ComicPython6045 Foundation.\nAll Rights Reserved.\n")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()

# ==========={准备工作}==================
import tkinter as tk
import os

root = tk.Tk()
root.title("Program for file=[12.29(春夏秋冬).py]")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============={创建函数或类}===============
def spring():
    label1.config(image=img1)


def summer():
    label1.config(image=img2)


def autumn():
    label1.config(image=img3)


def winter():
    label1.config(image=img4)


# ==========={主程序}==================

img1 = tk.PhotoImage(file=os.path.join(BASE_DIR, "素材", "春.png"))
img2 = tk.PhotoImage(file=os.path.join(BASE_DIR, "素材", "夏.png"))
img3 = tk.PhotoImage(file=os.path.join(BASE_DIR, "素材", "秋.png"))
img4 = tk.PhotoImage(file=os.path.join(BASE_DIR, "素材", "冬.png"))
label1 = tk.Label(root, image=img1)
button1 = tk.Button(root, text="春", font=("Microsoft JhengHei UI", 35, "bold"), bg="SpringGreen1", command=spring)
button2 = tk.Button(root, text="夏", font=("Microsoft JhengHei UI", 35, "bold"), bg="Red", command=summer)
button3 = tk.Button(root, text="秋", font=("Microsoft JhengHei UI", 35, "bold"), bg="Wheat1", command=autumn)
button4 = tk.Button(root, text="冬", font=("Microsoft JhengHei UI", 35, "bold"), bg="DodgerBlue1", command=winter)
label1.grid(row=0, column=0, columnspan=4)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=1, column=3)

root.mainloop()
