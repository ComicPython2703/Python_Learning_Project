# coding=utf-8
"""
Title= 分支算法
"""
if __name__ == '__main__':
    print("====================== RESTART:分支算法.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


def Copyright():
    print("\nCopyright (c) 2010-2024 ComicPython6405 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print()

# =========={准备工作}==================
list1 = [143, 123, 412, 573, 271, 433, 869, 133, 254, 421, 284, 139]


# ============={创建函数或类}===============
def get_max(max_list):
    return max(max_list)


def slist(list1):
    len_list = len(list1)
    if len_list <= 2:
        return get_max(list1)
    left_max = list1[:len_list // 2]
    right_max = list1[len_list // 2:]
    max_left = slist(left_max)
    max_right = slist(right_max)
    return get_max([max_left, max_right])


# ==========={诸城市}=================
if __name__ == '__main__':
    print(slist(list1))
