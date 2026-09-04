# coding=utf-8
# =========={准备工作}==================
import time
import tkinter as tk  # 把tkinter 叫做 tk

root = tk.Tk()  # 把tk 的名字叫做 root
root.title("Program for file=[11.17（TK动画）]")  # 修改标题
root.geometry('700x600')  # 修改大小
canvas = tk.Canvas(root, width=1920, height=1080, bg='SkyBlue')
canvas.pack()
canvas.create_polygon(50, 50, 50, 100, 100, 75, fill="red")
canvas.create_polygon(60, 60, 60, 200, 200, 85, fill="green")
canvas.create_rectangle(40, 40, 50, 50, fill='yellow')
for i in range(500):
    canvas.move(1, 0, 1)
    canvas.move(2, 1, 0)
    canvas.move(3, 1, 1)
    canvas.update()
    time.sleep(0.01)
root.mainloop()
