# coding=utf-8
# encoding=utf-8


if __name__ == '__main__':
    print("====================== RESTART:计算器.py =====================")
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
root.title("Program for file=[2025.1.5(计算器).py]")
result = tk.Label(root, text="结果", font=("Microsoft JhengHei Ui", 23), width=15, height=1)
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
print("[!]计算器已启动")
val = tk.IntVar()

r1 = tk.Radiobutton(root, text="+", value=1, variable=val)
r2 = tk.Radiobutton(root, text="-", value=2, variable=val)
r3 = tk.Radiobutton(root, text="x", value=3, variable=val)
r4 = tk.Radiobutton(root, text="÷", value=4, variable=val)


# ============{创建函数}===================
def calc():
    x = int(entry1.get())
    y = int(entry2.get())
    n = val.get()
    if n == 1:
        results = x + y
        print("结果是:", results)
    elif n == 2:
        results = x - y
        print("结果是:", results)
    elif n == 3:
        results = x * y
        print("结果是:", results)
    else:
        results = x / y
        print("结果是:", results)
    result.config(text=results)


# ==========={主程序}==================
bottom = tk.Button(root, text="计算", command=calc)
result.grid(row=3, column=1, columnspan=2)
entry1.grid(row=0, column=1, columnspan=2)
entry2.grid(row=1, column=1, columnspan=2)
r1.grid(row=2, column=0)
r2.grid(row=2, column=1)
r3.grid(row=2, column=2)
r4.grid(row=2, column=3)
bottom.grid(row=4, column=1, columnspan=2)
root.mainloop()
