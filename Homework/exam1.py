# -*- coding: utf-8 -*-
print("\nCopyright (c) 2010-2025 ComicPython6045 Communicate.\nAll Rights Reserved.\n")
# ^\d{4}-\d{2}-\d{2}$
import re
a=input("input sth:")
# noinspection RegExpDuplicateCharacterInClass
r = re.match(r'^\d{4}-\d{2}-\d{2}$', a)
try:
    print(r.group())
except AttributeError:
    print("fail")

