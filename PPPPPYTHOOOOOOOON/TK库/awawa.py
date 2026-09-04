# coding=utf-8
# encoding=utf-8
if __name__ == '__main__':
    print("====================== RESTART:测试.py =====================")
    print("已连接到 pydev 调试器(内部版本号 251.25410.159)")


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
root.title('文本框')
root.geometry('1900x1000')

# ==========={创建函数或类}==============
def mypopup(event):
    editmenu.tk_popup(event.x_root, event.y_root)


#撤消菜单命令执行的函数
def undo():
    global mytext
    mytext.event_generate("<<Undo>>")


#剪切菜单命令执行的函数
def cut():
    global mytext
    mytext.event_generate("<<Cut>>")


#复制菜单命令执行的函数
def copy():
    global mytext
    mytext.event_generate("<<Copy>>")


#粘贴菜单命令执行的函数
def paste():
    global mytext
    mytext.event_generate("<<Paste>>")


def find():
    global mytext
    mytext.event_generate("<<find>>")


# =========================================
#多行文本框及布局
mytext = tk.Text(root, undo=True)
mytext.pack(expand=1, fill=tk.BOTH)
#添加文件子菜单的下一级菜单
saver = tk.Menu(root)
saver.add_command(label="另存为")
#添加编辑子菜单
editmenu = tk.Menu(root)
editmenu.add_command(label="撤消", accelerator="Ctrl+Z", command=undo)
editmenu.add_separator()
editmenu.add_radiobutton(label="剪切", accelerator="Ctrl+X", command=cut)
editmenu.add_radiobutton(label="复制", accelerator="Ctrl+C", command=copy)
editmenu.add_command(label="粘帖", accelerator="Ctrl+V", command=paste)
editmenu.add_command(label="删除")
editmenu.add_separator()
editmenu.add_command(label="使用Bing搜索")
editmenu.add_command(label="查找", command=find)
editmenu.add_command(label="查找下一个")
editmenu.add_command(label="查找上一个")
editmenu.add_command(label="替换")
editmenu.add_command(label="转到")
editmenu.add_separator()
editmenu.add_checkbutton(label="全选")
editmenu.add_command(label="时间/日期")
#添加文件子菜单
filemenu = tk.Menu(root)
filemenu.add_command(label="新建")
filemenu.add_checkbutton(label="打开")
filemenu.add_cascade(label="保存", menu=saver)
filemenu.add_separator()
filemenu.add_radiobutton(label="页面设置", state=tk.DISABLED)
filemenu.add_separator()
filemenu.add_radiobutton(label="退出")
# 添加格式菜单
formartmenu = tk.Menu(root)
formartmenu.add_command(label="自动换行")
formartmenu.add_command(label="字体")
#添加顶级菜单
mymenu = tk.Menu(root)
mymenu.add_cascade(label="文件", menu=filemenu)
mymenu.add_cascade(label="编辑", menu=editmenu)
mymenu.add_cascade(label="格式", menu=formartmenu)
mymenu.add_cascade(label="查看")
mymenu.add_cascade(label="帮助")
#添加右键菜单命令
mytext.bind("<Button-3>", mypopup)
#把顶级菜单添加到窗体中
root["menu"] = mymenu
root.mainloop()

root.mainloop()
