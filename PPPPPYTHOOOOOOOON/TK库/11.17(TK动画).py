# coding=utf-8
# encoding=utf-8
"""
Title= TK库
"""
import tkinter as tk  # 把tkinter 叫做 tk

def animate_triangle(canvas, step=0, total_steps=500):
    """使用after实现的动画函数"""
    if step < total_steps:
        # 加快移动速度：每次移动3像素（原为1像素）
        move_distance = 3
        
        # 奇偶步控制移动方向
        if step % 2 == 0:
            canvas.move(1, 0, move_distance)  # 向下移动
        else:
            canvas.move(1, move_distance, 0)  # 向右移动
            
        # 减少延迟时间：从10毫秒减至5毫秒
        canvas.after(5, animate_triangle, canvas, step+1, total_steps)

def on_closing():
    """窗口关闭时的安全处理"""
    print("[TK][INFO]安全关闭窗口")
    root.destroy()

if __name__ == '__main__':
    print("====================== RESTART:TK动画.py =====================")
    print("\nCopyright (c) 2010-2024 ComicPython6045 Foundation.\nAll Rights Reserved.")
    
    def lesson(python):
        print(f'Hi,{python}')

    # =========={主窗口设置}==================
    root = tk.Tk()
    root.title("Program for file=[11.17（TK动画）]")
    root.geometry('700x600')
    root.protocol("WM_DELETE_WINDOW", on_closing)  # 注册关闭事件处理
    
    print("[TK][INFO]成功的启动TK窗口!")
    
    # 创建画布
    canvas = tk.Canvas(root, width=700, height=600, bg='SkyBlue')
    canvas.pack()
    
    # 创建图形（只移动红色三角形）
    canvas.create_polygon(50, 50, 50, 100, 100, 75, fill="red", tags="triangle")
    canvas.create_polygon(60, 60, 60, 200, 200, 85, fill="green")
    canvas.create_rectangle(50, 50, 200, 200)
    
    # 启动动画（速度加倍）
    animate_triangle(canvas)
    
    root.mainloop()
    lesson("Python")