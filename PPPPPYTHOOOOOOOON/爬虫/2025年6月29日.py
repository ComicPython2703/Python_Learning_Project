# coding=utf-8
# encoding=utf-8

if __name__ == '__main__':
    print("====================== RESTART:正则表达式P2.py =====================")
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
# =====================================
url1 = 'https://www.duitang.com/search/?kw=%E9%A3%8E%E6%9A%B4&type=feed'
headers = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
           'Safari/537.36 Edg/108.0.1462.54')
ss1 = '"<img src=https://grvferv.ccc/asd.jpg" alt="xxxxxx" data-x="1620 data-y="2400">'
res1 = re.search(r"https?://.*?\.jpg", ss1)
try:
    print(res1.group())
except AttributeError:
    print("[WARNING]匹配失败!")
