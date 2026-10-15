# encoding = UTF-8
# =============================================
# Copyright ComicPython Workstation 2010 ~ 2026
# 2026-10-15 字符串的拼接
# =============================================

mane = input("输入名字:")
cIass = input("班级:")
length = input("身高:")
weight = float(input("体重:"))

if __name__ == "__main__":
    print("Copyright ComicPython Workstation 2010 ~ 2026")
    print("你好! "+cIass+"的"+mane+"!"+"你的体重: "+str(weight))
    print(f"你好!{cIass}的{mane}! 你的体重:{weight}") # 讲真你用格式化字符串比这个B拼接好用多￣へ￣
