# coding=utf-8
# encoding=utf-8

if __name__ == '__main__':
    print("====================== RESTART:小学英语.py =====================")
# noinspection PyPep8Naming
def Copyright():
    print("\nCopyright (c) 2010-2025 ComicPython6045 Company & Education.\nAll Rights Reserved.\n")

def lesson(python):
    print(f'Hi,{python}')

if __name__ == '__main__':
    Copyright()

# ==========={准备工作}==================
import tkinter as tk
import random
from tkinter import messagebox
import os

root = tk.Tk()
root.title("⩽开心⩾背单词.py")
root.geometry('600x450')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

files = [
    os.path.join(BASE_DIR, "小学英语/三年级上.txt"),
    os.path.join(BASE_DIR, "小学英语/三年级下.txt"),
    os.path.join(BASE_DIR, "小学英语/四年级上.txt"),
    os.path.join(BASE_DIR, "小学英语/四年级下.txt"),
    os.path.join(BASE_DIR, "小学英语/五年级上.txt"),
    os.path.join(BASE_DIR, "小学英语/五年级下.txt"),
    os.path.join(BASE_DIR, "小学英语/六年级上.txt"),
    os.path.join(BASE_DIR, "小学英语/六年级下.txt"),
]
words_list = []


# ============={创建函数或类}==================
# noinspection PyPep8Naming
class MainFace:  # 主界面
    def __init__(self):
        self.create_widget()

    # noinspection PyAttributeOutsideInit
    def create_widget(self):  # 创建组件
        self.frame = tk.Frame(root)
        self.frame.pack()
        label1 = tk.Label(self.frame, text='⩽开心⩾背单词', font=("Microsoft JhengHei Ui", 23))
        label1.pack(pady=10)
        frame1 = tk.Frame(self.frame)
        frame1.pack(padx=20, pady=10, side=tk.LEFT)
        self.v = tk.IntVar()
        tk.Radiobutton(frame1, text="小学英语/三上", variable=self.v, value=0,
                       font=("Microsoft JhengHei Ui", 18)).pack()
        tk.Radiobutton(frame1, text="小学英语/三下", variable=self.v, value=1,
                       font=("Microsoft JhengHei Ui", 18)).pack()
        tk.Radiobutton(frame1, text="小学英语/四上", variable=self.v, value=2,
                       font=("Microsoft JhengHei Ui", 18)).pack()
        tk.Radiobutton(frame1, text="小学英语/四下", variable=self.v, value=3,
                       font=("Microsoft JhengHei Ui", 18)).pack()
        tk.Radiobutton(frame1, text="小学英语/五上", variable=self.v, value=4,
                       font=("Microsoft JhengHei Ui", 18)).pack()
        tk.Radiobutton(frame1, text="小学英语/五下", variable=self.v, value=5,
                       font=("Microsoft JhengHei Ui", 18)).pack()
        tk.Radiobutton(frame1, text="小学英语/六上", variable=self.v, value=6,
                       font=("Microsoft JhengHei Ui", 18)).pack()
        tk.Radiobutton(frame1, text="小学英语/六下", variable=self.v, value=7,
                       font=("Microsoft JhengHei Ui", 18)).pack()
        frame2 = tk.Frame(self.frame)
        frame2.pack(padx=20, pady=20, side=tk.RIGHT)
        b1 = tk.Button(frame2, text="开始学习", command=self.goto_study_face, font=("Microsoft JhengHei Ui", 23),
                       width=15, height=1)
        b2 = tk.Button(frame2, text="开始测试", command=self.goto_test_face, font=("Microsoft JhengHei Ui", 23),
                       width=15, height=1)
        b3 = tk.Button(self.frame, text="X", command=exit)
        b1.pack()
        b2.pack(pady=10)
        b3.pack(side=tk.BOTTOM)  # 👆🤓

    def goto_study_face(self):  # 去学习界面
        print("正在启动学习界面.....")
        self.readfile()
        self.frame.destroy()

        StudyFace()

    def goto_test_face(self):  # 去测试界面🤔
        print("正在启动测试界面.....")
        self.readfile()
        self.frame.destroy()
        TestFace()

    def readfile(self):
        words_list.clear()  # 清空列表
        filename = files[self.v.get()]  # 选择年级
        # 添加文件存在检查
        if not os.path.exists(filename):
            error_msg = f"找不到单词文件:\n{filename}\n请确保文件存在！"
            messagebox.showerror("文件错误", error_msg)
            print(error_msg)
            return
        try:
            with open(filename, "rt", encoding="utf-8") as f:  # 打开文件,as="别名":
                lines = f.readlines()  # 必须加s,否则无法读取单词数据!!!!
                print("正在加载单词数据...")
                for lines in lines:
                    words = lines.split(",")
                    for i in range(len(words)):
                        words[i] = words[i].strip()  # 去除空格
                    words_list.append(words)  # 处理后的单词放入列表
            print("本次单词数据:", words_list)
        except Exception as e:
            messagebox.showerror("文件错误", f"读取文件失败:\n{str(e)}")
            print("===========================================================")
            print(f"读取文件失败: {str(e)}")
            print("===========================================================")


# noinspection PyTypeChecker
class StudyFace:  # 学习界面
    def __init__(self):
        self.cheat = 0
        self.wordss = None
        self.words_list = words_list
        self.word_eg = tk.StringVar()
        self.word_ch = tk.StringVar()
        self.word_po = tk.StringVar()
        self.ceate_widget()
        self.new_word()

    def ceate_widget(self):
        # noinspection PyAttributeOutsideInit
        self.frame = tk.Frame(root)
        self.frame.pack()

        # 显示标题
        ll1 = tk.Label(self.frame, text="背单词", font=("Microsoft JhengHei Ui", 32))
        ll1.pack(pady=20)

        # 单词及音标
        frame1 = tk.Frame(self.frame)
        frame1.pack()
        # noinspection PyAttributeOutsideInit
        self.label1 = tk.Label(frame1, textvariable=self.word_eg, font=("Microsoft JhengHei Ui", 40))
        # noinspection PyAttributeOutsideInit
        self.label2 = tk.Label(frame1, textvariable=self.word_po, font=("Microsoft JhengHei Ui", 12))
        # noinspection PyAttributeOutsideInit
        self.label3 = tk.Label(frame1, textvariable=self.word_ch, font=("Microsoft JhengHei Ui", 24))
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        self.label2.grid(row=1, column=0)
        self.label3.grid(row=2, column=0, padx=10, pady=10)

        # 知道和不知道按钮
        frame2 = tk.Frame(self.frame)
        frame2.pack()
        # noinspection PyAttributeOutsideInit
        self.button1 = tk.Button(frame2, text="知道", font=("Microsoft JhengHei Ui", 18), width=10, command=self.know)
        # noinspection PyAttributeOutsideInit
        self.button2 = tk.Button(frame2, text="不知道", font=("Microsoft JhengHei Ui", 18), width=10,
                                 command=self.dont_know)
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)

        # 返回
        frame3 = tk.Frame(self.frame)
        frame3.pack()
        b1 = tk.Button(frame3, text="返回", command=self.go_back, font=("Microsoft JhengHei Ui", 17))
        b1.grid(pady=10)

    def go_back(self):
        self.frame.destroy()
        MainFace()
        print("[MainFace]正在返回主界面......")
        print("[MainFace]完成!")

    def new_word(self):
        if words_list:
            self.wordss = random.choice(words_list)
            print("待学习:", self.wordss)
            self.word_eg.set(self.wordss[0])
            self.word_po.set(self.wordss[1])
            self.word_ch.set("")
        else:
            messagebox.showinfo("小学英语.学习界面", "学习完成,即将进入测试")
            TestFace()

    def know(self):
        try:
            self.word_ch.set(self.wordss[2])
            self.words_list.remove(self.wordss)
            self.frame.after(500, self.new_word)
        # print("[INFO]点按的是知道,删除并继续")
        except ValueError:
            print("[StudyFace][Warning]你按得太快了!")
            self.cheat += 1
            if self.cheat == 10:
                print("\nTraceback (most recent call last):")
                print('  File "E:\Python\PPPPPYTHOOOOOOOON\TK库\ 2025.1.19(小学英语).py", line 201, in <module>')
                print("illegal Cheat")
                print("进程已结束，退出代码为 -15894597 (0xC000015A: interrupted by Too many errors!)")
                tk.messagebox.showerror("PythonCrashMessageBox", "Cheat")
                breakpoint()

    def dont_know(self):
        self.word_ch.set(self.wordss[2])
        self.frame.after(1000, self.new_word)


class TestFace:  # 单词测试界面
    def __init__(self):
        self.health = 10
        self.index = None
        self.v = None
        self.frame = tk.Frame(root)
        self.word_eg = tk.StringVar()  # 实时显示变量内值的变化
        self.word_sound = tk.StringVar()
        self.word_ch_0 = tk.StringVar()
        self.word_ch_1 = tk.StringVar()
        self.word_ch_2 = tk.StringVar()
        self.word_ch_3 = tk.StringVar()
        random.shuffle(words_list)  # 从单词列表内随机选择单词
        self.count = 0  # 单词计数
        self.create_widget()
        self.new_word()

    def create_widget(self):
        # 创建主标题的框架
        self.frame.pack()
        tk.Label(self.frame, text="单词测试", font=("Microsoft JhengHei Ui", 32)).pack()
        # 创建用于显示单词的框架
        frame1 = tk.Frame(self.frame)
        frame1.pack()
        tk.Label(frame1, textvariable=self.word_eg, font=("Microsoft JhengHei Ui", 40)).grid(row=0, column=0)
        # 展示音标的框架
        tk.Label(frame1, textvariable=self.word_sound, font=("Microsoft JhengHei Ui", 12)).grid(row=1, column=0)
        self.v = tk.IntVar()  # 创建整型内置变量
        frame2 = tk.Frame(self.frame)
        frame2.pack()
        tk.Radiobutton(frame2, variable=self.v, value=0, textvariable=self.word_ch_0,
                       font=("Microsoft JhengHei Ui", 22), command=self.check).grid(row=3,
                                                                                    column=0,
                                                                                    padx=20,
                                                                                    pady=10,
                                                                                    stick=tk.W)
        tk.Radiobutton(frame2, variable=self.v, value=1, textvariable=self.word_ch_1,
                       font=("Microsoft JhengHei Ui", 22), command=self.check).grid(row=3,
                                                                                    column=1,
                                                                                    padx=20,
                                                                                    pady=10,
                                                                                    stick=tk.W)
        tk.Radiobutton(frame2, variable=self.v, value=2, textvariable=self.word_ch_2,
                       font=("Microsoft JhengHei Ui", 22), command=self.check).grid(row=4,
                                                                                    column=0,
                                                                                    padx=20,
                                                                                    pady=10,
                                                                                    stick=tk.W)
        tk.Radiobutton(frame2, variable=self.v, value=3, textvariable=self.word_ch_3,
                       font=("Microsoft JhengHei Ui", 22), command=self.check).grid(row=4,
                                                                                    column=1,
                                                                                    padx=20,
                                                                                    pady=10,
                                                                                    stick=tk.W)
        frame3 = tk.Frame(self.frame)
        frame3.pack()
        tk.Button(frame3, text="返回", command=self.back,
                  font=("Microsoft JhengHei Ui", 22)).grid(row=1, column=0, padx=10, pady=10)

    def new_word(self):
        print("剩余生命值:", self.health)
        if self.count >= len(words_list):
            tk.messagebox.showinfo('提示', '测试已结束')
            self.back()
        else:
            # 新单词展示
            self.v.set(-1)  # 默认选项清空
            word = words_list.pop(0)  # 移除列标中的第一个元素，并返回这个元素赋值给变量word
            self.word_eg.set(word[0])  # 将新列表word中的第0项，英文单词设置为题目
            self.word_sound.set(word[1])  # 将新列表word中的第1项，音标设置为题目
            self.index = random.randint(0, 3)  # 在0,1,2,3中随机一个数
            words = random.sample(words_list, 3)  # 从剩余单词列表中随机选择3个单词作为干扰项
            words.insert(self.index, word)  # 随机插入0,1,2,3中某一位置
            self.word_ch_0.set(words[0][2])  # 将所有汉语设置位选项
            self.word_ch_1.set(words[1][2])
            self.word_ch_2.set(words[2][2])
            self.word_ch_3.set(words[3][2])
            words_list.append(word)  # 将列表最前面被移除的元素放到列表的末尾。
            self.count += 1

    def check(self):
        if 0 <= self.v.get() <= 3:  # 如果不选任何选项点确认，不做任何反馈
            if self.index == self.v.get():
                tk.messagebox.showinfo('结果', '正确')
            else:
                tk.messagebox.showerror('结果', '错误')
                self.health -= 1
                if self.health == 0:
                    print("\nTraceback (most recent call last):")
                    print('  File "E:\Python\PPPPPYTHOOOOOOOON\TK库\ 2025.1.19(小学英语).py", line 303, in <module>')
                    print("TrackLost")
                    print("进程已结束，退出代码为 -15894597 (0xC000015A: interrupted by Too many errors!)")
                    tk.messagebox.showerror("PythonCrashMessageBox", "TrackLost")
                    breakpoint()
            self.new_word()

    def back(self):  # 返回主界面
        self.frame.destroy()
        MainFace()
        print("[MainFace]正在返回主界面......")
        print("[MainFace]完成!")


# ============{主程序}=======================
# 👆🤓
print("[MainFace]启动了主程序")

if __name__ == '__main__':
    MainFace()
    root.mainloop()
    lesson("Python")


