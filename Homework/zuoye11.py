# coding=utf-8
import tkinter as tk

root = tk.Tk()
root.title("Program for file=[12.15（单选框）.py]")
root.geometry('700x600')
label1 = tk.Label(root, text="百度", font=("Microsoft JhengHei Ui", 20))
label2 = tk.Label(root,
                  text="百度（Baidu）是拥有强大互联网基础的领先AI公司。百度愿景是：成为最懂用户，并能帮助人们成长的全球顶级高科技公司。 \n"
                       "1]“百度”二字，来自于八百年前南宋词人辛弃疾的一句词：众里寻他千百度。\n这句话描述了词人对理想的执着追求。1999\n"
                       "年底，身在美国硅谷的李彦宏看到了中国互联网及中文搜索引擎服务的巨大发展潜力，抱着技术改变世界的梦想\n，他毅然辞掉硅谷的高薪工作，携搜索引擎专利技术，于2000年1月1\n"
                       "日在中关村创建了百度公司。", font=("Microsoft JhengHei Ui", 10))

photo = tk.PhotoImage(file="素材/Baidu_Logo.png")
label3 = tk.Label(root, image=photo)
label1.pack()
label2.pack(side=tk.LEFT)
label3.pack(side=tk.RIGHT)
# —————————————————————————————
root.mainloop()
