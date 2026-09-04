# coding=utf-8
import tkinter as tk
import random

# 垃圾类型，1表示可回收，2表示有害垃圾，3表示厨余垃圾，4表示其他垃圾
wastes = [["手机", 1], ["牛奶盒", 1], ["塑料瓶", 1], ["易拉罐", 1],
          ["干电池", 2], ["药品", 2], ["指甲油", 2], ["药瓶", 2],
          ["玉米棒", 3], ["鸡蛋壳", 3], ["树叶", 3], ["鸡骨头", 3],
          ["塑料袋", 4], ["卫生纸", 4], ["旧口罩", 4], ["纸杯", 4]]

# 画布宽高
width = 800
height = 600


class Window:
    def __init__(self, root):
        self.sun_x1 = None
        self.score_text = None
        self.score = None
        self.c = None
        self.root = root
        self.root.title('垃圾分类')
        self.create_widget()
        self.create_bg()
        self.create_waste_can()  # 创建垃圾桶
        self.create_waste()  # 创建垃圾
        self.move_waste()  # 移动垃圾
        self.check_catch()  # 碰撞检测

    def create_widget(self):
        tk.Label(self.root, text="垃圾分类", font=(None, 40)).pack()  # 文字标签
        self.c = tk.Canvas(root, width=width, height=height, bg="skyblue")  # 创建一个画布
        self.c.pack()

        self.c.focus_set()  # 设定焦点
        self.c.bind("<Key-Left>", self.move_left)  # 左方向键向左移动垃圾桶
        self.c.bind("<Key-Right>", self.move_right)  # 右方向键向右移动垃圾桶
        self.c.bind("<Key>", self.change_bin)  # 改变垃圾桶类型

        self.score = 0  # 游戏得分
        self.score_text = self.c.create_text(700, 50, text=str(self.score), font=(None, 32), fill="white")

    def create_bg(self):  # 创建游戏背景
        # 草地
        self.c.create_rectangle((-5, height - 100, width + 5, height + 5), fill='seagreen', width=0)
        # 太阳
        self.sun_x1, self.sun_y1, self.sun_x2, self.sun_y2 = 0, 0, 120, 120
        self.sun = self.c.create_oval(self.sun_x1, self.sun_y1, self.sun_x2, self.sun_y2, fill='gold', width=0)
        # 树1
        self.c.create_rectangle(280, 400, 320, 520, fill='sienna', width=0)  # 树干
        self.c.create_polygon(180, 400, 420, 400, 300, 300, fill='limegreen', width=0)  # 树叶1
        self.c.create_polygon(200, 320, 400, 320, 300, 220, fill='limegreen', width=0)  # 树叶2
        # 树2
        self.tree_x1, self.tree_y1, self.tree_x2, self.tree_y2 = 600, 210, 800, 420
        self.c.create_rectangle(680, 400, 720, 520, fill='sienna', width=0)  # 树干
        self.tree = self.c.create_oval(self.tree_x1, self.tree_y1, self.tree_x2, self.tree_y2, fill='green', width=0)

        self.tree_r = 1  # 树幅度值
        self.effect()
        self.effect_sun()

    def effect(self):  # 树摇动
        self.tree_x1 -= self.tree_r
        self.tree_x2 += self.tree_r
        self.tree_y1 += self.tree_r
        self.tree_y2 -= self.tree_r
        if self.tree_x1 < 598 or self.tree_x1 > 602:
            self.tree_r = -self.tree_r

        self.c.coords(self.tree, self.tree_x1, self.tree_y1, self.tree_x2, self.tree_y2)
        self.root.after(100, self.effect)

    def effect_sun(self):  # 太阳动
        self.sun_x1 -= self.tree_r
        self.sun_x2 += self.tree_r
        self.sun_y1 -= self.tree_r
        self.sun_y2 += self.tree_r
        self.c.coords(self.sun, self.sun_x1, self.sun_y1, self.sun_x2, self.sun_y2)

        self.root.after(300, self.effect_sun)

    def create_waste_can(self):  # 创建垃圾桶
        self.x1 = 400  # 垃圾桶横坐标
        self.y1 = 520  # 垃圾桶纵坐标
        self.waste_bin = self.c.create_image(self.x1, self.y1, image=kehuishou)
        self.waste_bin_type = 1  # 垃圾桶类型

    def move_left(self, event):  # 向左移动垃圾桶
        self.x1 -= 10
        if self.x1 <= 0:
            self.x1 = 0
        self.c.coords(self.waste_bin, self.x1, self.y1)

    def move_right(self, event):  # 向右移动垃圾桶
        self.x1 += 10
        if self.x1 >= width:
            self.x1 = width
        self.c.coords(self.waste_bin, self.x1, self.y1)

    def change_bin(self, event):  # 按键改变垃圾桶的类型
        if event.char == "1":  # 如果按下的按键是 1
            self.c.itemconfig(self.waste_bin, image=kehuishou)  # 改变垃圾桶图片
            self.waste_bin_type = 1  # 改变垃圾桶类型标志
        elif event.char == "2":
            self.c.itemconfig(self.waste_bin, image=youhai)
            self.waste_bin_type = 2
        elif event.char == "3":
            self.c.itemconfig(self.waste_bin, image=chuyu)
            self.waste_bin_type = 3
        elif event.char == "4":
            self.c.itemconfig(self.waste_bin, image=qita)
            self.waste_bin_type = 4

    def create_waste(self):  # 创建垃圾
        self.x2 = random.randrange(20, 780, 10)
        self.y2 = 10
        waste = random.choice(wastes)
        self.waste = self.c.create_text(self.x2, self.y2, text=waste[0], fill="white", font=(None, 10))
        self.waste_type = waste[1]

    def move_waste(self):  # 移动垃圾 没接住
        self.y2 += 5
        self.c.coords(self.waste, self.x2, self.y2)
        if self.y2 > self.y1:
            self.score -= 10
            self.c.itemconfig(self.score_text, text=str(self.score))
            self.c.delete(self.waste)
            self.create_waste()
            # 闪屏特效
            self.c.config(bg="red")
            self.root.after(50, lambda: self.c.config(bg="skyblue"))
        root.after(50, self.move_waste)

    def check_catch(self):  # 碰撞检测
        if (self.x1 - 40 < self.x2 < self.x1 + 40) and (self.y1 - 30 < self.y2 < self.y1):  # 碰撞条件
            if self.waste_bin_type == self.waste_type:
                self.score += 10
            else:
                self.score -= 10
                self.c.config(bg="red")
                self.root.after(100, lambda: self.c.config(bg="skyblue"))
            self.c.itemconfig(self.score_text, text=str(self.score))
            self.c.delete(self.waste)
            self.create_waste()
        root.after(50, self.check_catch)  # 在100毫秒后，再次调用这个函数


root = tk.Tk()

kehuishou = tk.PhotoImage(file="PNG/kehuishou.png")
youhai = tk.PhotoImage(file="PNG/youhai.png")
chuyu = tk.PhotoImage(file="PNG/chuyu.png")
qita = tk.PhotoImage(file="PNG/qita.png")

Window(root)
root.mainloop()
