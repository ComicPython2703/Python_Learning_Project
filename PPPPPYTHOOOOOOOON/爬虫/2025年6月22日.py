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
#
ss1="123 six six six 周日学C++"
res1=re.match(r"^\d.*\W$",ss1)
#
wwww="wvuiiashcd,.nocnoncvsncsaj,.vjfvoi,.ajcoiavoijfioejriuy43qutiywuyiuyreiuytpqecnxbz,mbzjkdsalkfhadfgiuefiudiuvxz"
# ============{创建函数}===============
def a():
    count=0
    for i in wwww:
        r = re.match(r"\w", i)
        if r:
            count += 1
    print(count)
# ============{主程序}===================
try:
    print("res1的结果为：",res1.group())
except AttributeError:
    print("[AttributeError]匹配失败!")
a()
