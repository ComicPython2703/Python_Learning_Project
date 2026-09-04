# -*- coding: utf-8 -*-
print("Copyright (c) 2010-2025 ComicPython6045 Communicate.\nAll Rights Reserved.\n")


def lesson(python):
    print(f'Hi,{python}')


import re

a = ['data.dat',
     'data1.dat',
     'data2.dat',
     'data12.dat',
     'datax.dat',
     'dataXYZ.dat',
     'dataN.dat']

for i in a:
    r = re.match(r'data\w?\.dat', i)  # 使用原始字符串(raw string)修复转义问题
    try:
        print(r.group())
    except AttributeError:
        pass
