# coding=utf-8
# coding=utf-8
# encoding=utf-8
"""
Title= TK库
"""
if __name__ == '__main__':
    print('正在运行程式：D:\Python38\python.exe -X pycache_prefix=C:\ '
          'Users\EDY\AppData\Local\JetBrains\PyCharmCE2024.1\cpython-cache "C:/Program Files/JetBrains/PyCharm '
          'Community Edition 2024.1.2/plugins/python-ce/helpers/pydev/pydevd.py" --multiprocess --qt-support=auto '
          '--client 127.0.0.1 --port 50945 --file "E:\Python\PPPPPYTHOOOOOOOON\ TK库\ 11.10 (TK库).py" ')
    print("====================== RESTART:TK库.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


def Copyright():
    print("\nCopyright (c) 2010-2024 ComicPython6405 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print()

# =========={准备工作}==================
import tkinter as tk  # 把tkinter 叫做 tk

root = tk.Tk()  # 把tk 的名字叫做 root
root.title("Program for file=[11.10（TK库）]")  # 修改标题
root.geometry('700x600')  # 修改大小
# ============{创建函数}=================
# ==========={主程试}=================
if __name__ == '__main__':
    print("[TK][INFO]成功的启动TK窗口!")
    # 创建画布
    canvas = tk.Canvas(root, width=1920, height=1080, bg='SkyBlue')
    canvas.pack()
    # 绘制矩形
    canvas.create_rectangle(50, 50, 200, 200)
    canvas.create_line(50, 200, 200, 50)
    canvas.create_line(50, 50, 200, 200)
    # 绘制多边形
    canvas.create_polygon(0, 0, 0, 30, 30, 30, 30, 0)
    # 坐标                         ( x1,y1, x2,y2 ,x3 , y3  , x4,y4)
    # 创建圆形
    canvas.create_oval(200, 100, 300, 300)  # 画椭圆
    canvas.create_oval(300, 200, 500, 400)  # 画圆
    canvas.create_arc(300, 200, 500, 400, start=5, extent=50)
    canvas.create_arc(300, 200, 500, 400, start=1245, extent=34)
    # 创建弧形          (圆形坐标                        ,start=初始角度,extent=增加角度)
    root.mainloop()
    lesson("Python")
