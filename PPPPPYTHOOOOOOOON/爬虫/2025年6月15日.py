# coding=utf-8
# encoding=utf-8
if __name__ == '__main__':
    print("====================== RESTART:正则表达式.py =====================")
    print("已连接到 pydev 调试器(内部版本号 251.25410.159)")


# noinspection PyPep8Naming
def Copyright():
    print("\nCopyright (c) 2010-2025 ComicPython6045 Communicate.\nAll Rights Reserved.\n")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
# ==========={准备工作}==================
import re

s1 = "abcd"
s2 = "a123"
s3 = "aaa"
s4 = "abbe"
# ————————————————
s5 = "a123b"
# =========={主程序}===================

res = re.match(r"a[a-z|A-Z]", s1)  # 根据自己定义的正则表达式匹配
res1 = re.match(r"a\d\d\db", s5)

try:
    print("s1匹配到之后提取内容为:", res.group())  # 匹配到之后提取内容
    print("s2匹配到之后提取内容为:", res1.group())
except AttributeError:
    print("[AttributeError]匹配失败!")
