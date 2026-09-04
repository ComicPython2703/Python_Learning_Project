# coding=utf-8
# encoding=utf-8
# 不要看这里!!!!

if __name__ == '__main__':
    print("====================== RESTART:计算器.py =====================")
    print("已连接到 pydev 调试器(内部版本号 243.23654.177)")


# 不要看这里!!!!


# noinspection PyPep8Naming
def Copyright():
    print("\nCopyright (c) 2010-2025 ComicPython6045 Communicate.\nAll Rights Reserved.\n")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()

# ==========={准备工作}==================
import tkinter as tk

root = tk.Tk()


# ==========={创建函数或类}==============
class window:
    def __init__(self):
        self.tree_r = None
        self.sun = None
        self.c = None

        self.root = root
        self.root.width = 800
        self.root.height = 600

        self.root.title("垃圾分类.py")
        self.create_widget()
        self.create_bg()  # 必须调用,否则没有草地

    def create_widget(self):
        tk.Label(self.root, text="垃圾分类", font=("Microsoft JhengHei Ui", 40)).pack()
        self.c = tk.Canvas(root, width=800, height=600, bg="skyblue")
        self.c.pack()

    def create_bg(self):
        # noinspection PyAttributeOutsideInit
        self.tree_x1, self.tree_y1, self.tree_x2, self.tree_y2 = 600, 210, 800, 420
        # 树1
        self.c.create_rectangle(280, 400, 320, 520, fill="sienna", width=0)
        self.c.create_polygon(180, 400, 420, 400, 300, 300, fill="green", width=0)
        self.c.create_polygon(180, 320, 420, 320, 300, 220, fill="green", width=0)
        # 树2
        self.c.create_rectangle(680, 400, 720, 520, fill="sienna", width=0)
        self.c.create_oval(600, 210, 800, 420, fill="green", width=0)
        # 草地
        self.c.create_rectangle(-5, 500, 805, 605, fill="seagreen", width=0)
        # 太阳
        self.sun = self.c.create_oval(0, 0, 120, 120, fill="red", width=0)
        self.tree_r = 1
        self.effect()
        self.effect_sun()

    def effect(self):
        self.tree_x1-=self.tree_r                            #x=x-1 or x-=1
        self.tree_y1 -= self.tree_r
        self.tree_x2-= self.tree_r
        self.tree_y2 -= self.tree_r
        if self.tree_x1 < 598 or self.tree_x1 > 602:
            self.tree_r =- self.tree_r

    def effect_sun(self):
        pass


# ==========={主程序}=============
window()
root.mainloop()
