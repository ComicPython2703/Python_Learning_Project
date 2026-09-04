# coding=utf-8
# encoding=utf-8


if __name__ == '__main__':
    print("====================== RESTART:名片制作.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


def Copyright():
    print("\nCopyright (c) 2010-2025 ComicPython6045 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print("乐小美.png 仅供给此文件!")
"""
乐小美.png 仅供给此文件!
"""
# ==========={准备工作}==================
import tkinter as tk
import os
root = tk.Tk()
root.title("Program for file=[12.29（名片制作）.py]")
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "素材", "乐小美.png")
# ==========={主程序}==================
img = tk.PhotoImage(file=image_path)  # 添加图像
label1 = tk.Label(root, image=img)
label2 = tk.Label(root, text="小帅", font=("Microsoft JhengHei UI", 40, "bold"))
label3 = tk.Label(root, text="大三", font=("Microsoft JhengHei UI", 20))
label4 = tk.Label(root, text="QQ:893752098", font=("Microsoft JhengHei UI", 10))
label5 = tk.Label(root, text="德智体美劳全面发展,", font=("Microsoft JhengHei UI", 10))
label6 = tk.Label(root, text="学习好,有礼貌,", font=("Microsoft JhengHei UI", 10))
label7 = tk.Label(root, text="爱好广泛,有爱心", font=("Microsoft JhengHei UI", 10))
label1.grid(row=3, column=0)  # row=行   column=列
label2.grid(row=0, column=0)
label3.grid(row=1, column=0)
label4.grid(row=2, column=0)  # qq
label5.grid(row=4, column=0)
label6.grid(row=5, column=0)
label7.grid(row=6, column=0)
root.mainloop()
