# coding=utf-8
import tkinter as tk

root = tk.Tk()
root.title("Program for file=[12.1（图形化设计）.py]")
root.geometry('700x600')
sstr = tk.StringVar()
label1 = tk.Text(root, font=("Microsoft JhengHei Ui", 23), height=3)
label1.pack()
click = 0
click2 = 0
entry1 = tk.Entry(root)
entry1.pack()


def on_click():
    global click
    if click == 0:
        label1.insert("insert", "二Greer")
        click = 1
    else:
        label1.insert("insert", "而顾问服务")
        click = 0


button1 = tk.Button(root, bg="red", text="启动字符二", font=("Microsoft JhengHei Ui", 23), width=15, height=4,
                    command=on_click)
button1.pack()
button2 = tk.Button(root, bg="blue", text="启动字符1", font=("Microsoft JhengHei Ui", 23), width=15, height=4,
                    command=on_click)
button2.pack()
root.mainloop()
