# coding=utf-8
# encoding=utf-8
"""
Title= 火箭发射
"""
if __name__ == '__main__':
    print("====================== RESTART:火箭发射.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


def Copyright():
    print("\nCopyright (c) 2010-2024 ComicPython6045 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print()

# =========={准备工作}==================
import tkinter as tk  # 把tkinter 叫做 tk
import time


# ==========={创建函数}===============
def rocket():
    root = tk.Tk()  # 把tk 的名字叫做 root
    root.title("Program for file=[11.24（火箭发射）]-Part-1")  # 修改标题
    canvas = tk.Canvas(root, width=1920, height=1080, bg='SkyBlue')
    canvas.pack()
    canvas.create_polygon(350, 450, 400, 450, 375, 400)
    canvas.create_rectangle(350, 450, 400, 700, fill="white")
    canvas.create_polygon(350, 700, 350, 600, 300, 700)
    canvas.create_polygon(400, 700, 450, 700, 400, 600)
    canvas.create_text(375, 500, text="中", font=("黑体", 30))
    canvas.create_text(375, 550, text="国", font=("黑体", 30))
    canvas.create_text(375, 600, text="航", font=("黑体", 30))
    canvas.create_text(375, 650, text="天", font=("黑体", 30))
    canvas.create_polygon(350, 700, 360, 700, 355, 720, fill="red")
    canvas.create_polygon(400, 700, 390, 700, 395, 720, fill="red")
    for i in range(500):
        for j in range(1, 11):
            canvas.move(j, 0, -2)
        canvas.update()
        time.sleep(0.01)
    root.mainloop()


# ==========={主程试}=================
window = tk.Tk()
window.title("启动器")  # 修改标题
button = tk.Button(window, text="启动", width=30, height=3, bg='red', command=rocket)
button.pack()
window.mainloop()
lesson('python')
