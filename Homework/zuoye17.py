# coding=utf-8
import re
a=input("输入邮箱|Enter e-mail：")
# noinspection RegExpDuplicateCharacterInClass,RegExpRedundantClassElement
res=re.match(r"[a-z|A-Z|\d]{6,16}@.{2,5}com",a)
try:
    print(res.group())
except AttributeError:
    print("非法邮箱！")