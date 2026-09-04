# coding=utf-8
# encoding=utf-8
# 不要看这里!!!!
from tkinter.constants import HIDDEN, NORMAL

if __name__ == '__main__':
    print("====================== RESTART:计算器.py =====================")
    print("已连接到 pydev 调试器(内部版本号 243.23654.177)")


# 不要看这里!!!!


# noinspection PyPep8Naming
def Copyright():
    print("\nCopyright (c) 2010-2025 ComicPython6045 Company & Education.\nAll Rights Reserved.\n")


# 不要看这里!!!!


def lesson(python):
    print(f'Hi,{python}')


# 不要看这里!!!!


if __name__ == '__main__':
    Copyright()

# ==========={准备工作}==================
import tkinter as tk

root = tk.Tk()


# ==========={创建函数或类}==============
class Window:
    def __init__(self):
        self.cheek_right = None
        self.cheek_left = None
        self.pupil_right = None
        self.pupil_left = None
        self.eyeright = None
        self.eyeleft = None
        self.mouth = None

        self.c = tk.Canvas(root, background="white",
                           width=800, height=600)  # 为了修 实例特性 c 在 __init__ 外部定义 的爆黄
        self.root = root

        self.root.title("屏幕宠物.py")
        self.create_widget()
        self.cccat()
        self.Blanking_eyes()

    def create_widget(self):
        self.c.pack()
        # self.c.bind()

    def cccat(self):
        #  耳朵
        self.c.create_polygon(110, 40, 100, 120, 190, 120, outline="black", fill="skyblue")
        self.c.create_polygon(290, 40, 300, 120, 210, 120, outline="black", fill="skyblue")
        # 身体
        self.c.create_oval(60, 80, 340, 320, outline="black", fill="skyblue")

        # 眼睛和瞳孔
        # 眼睛
        self.eyeleft = self.c.create_oval(120, 130, 180, 170, outline="black", fill="white")
        self.eyeright = self.c.create_oval(280, 130, 220, 170, outline="black", fill="white")
        # 瞳孔
        self.pupil_left = self.c.create_oval(140, 145, 160, 165, outline="black", fill="black")
        self.pupil_right = self.c.create_oval(260, 145, 240, 165, outline="black", fill="black")

        # 嘴巴
        # noinspection PyArgumentList
        self.mouth = self.c.create_line(170, 270, 200, 280, 230, 270, smooth=True)
        # 胡须
        self.c.create_line(90, 220, 40, 200)
        self.c.create_line(90, 230, 40, 230)
        self.c.create_line(90, 240, 40, 260)
        self.c.create_line(310, 220, 360, 200)
        self.c.create_line(310, 230, 360, 230)
        self.c.create_line(310, 240, 360, 260)
        self.cheek_left = self.c.create_oval(110, 200, 160, 250, outline="red", fill="red")
        self.cheek_right = self.c.create_oval(240, 200, 290, 250, outline="red", fill="red")
        # 红脸

    # noinspection PyPep8Naming
    def Closing_eyes(self):
        self.c.itemconfig(self.pupil_left, state=HIDDEN)
        self.c.itemconfig(self.pupil_right, state=HIDDEN)
        self.c.itemconfig(self.eyeright, fill="skyblue")
        self.c.itemconfig(self.eyeleft, fill="skyblue")

    # noinspection PyPep8Naming
    def Opening_eyes(self):
        self.c.itemconfig(self.pupil_left, state=NORMAL)
        self.c.itemconfig(self.pupil_right, state=NORMAL)
        self.c.itemconfig(self.eyeright, fill="white")
        self.c.itemconfig(self.eyeleft, fill="white")

    # noinspection PyTypeChecker,PyPep8Naming
    def Blanking_eyes(self):
        self.Closing_eyes()
        self.root.after(250, self.Opening_eyes)
        self.root.after(3000, self.Blanking_eyes)


# ==========={主程序}===============

if __name__ == '__main__':
    Window()

root.mainloop()
