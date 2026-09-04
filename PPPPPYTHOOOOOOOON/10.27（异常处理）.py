# coding=utf-8
"""
Title= 异常处理
"""
if __name__ == '__main__':
    print('正在运行程式：D:\Python38\python.exe -X pycache_prefix=C:\ '
          'Users\EDY\AppData\Local\JetBrains\PyCharmCE2024.1\cpython-cache "C:/Program Files/JetBrains/PyCharm '
          'Community Edition 2024.1.2/plugins/python-ce/helpers/pydev/pydevd.py" --multiprocess --qt-support=auto '
          '--client 127.0.0.1 --port 50945 --file "E:\Python\PPPPPYTHOOOOOOOON\ 10.27 (异常处理).py" ')
    print("====================== RESTART:异常处理.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


def Copyright():
    print("\nCopyright (c) 2010-2024 ComicPython6405 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


Copyright()
print()


# =========={准备工作}==================

# ============={创建函数或类}===============
def fun1(x, y):
    try:
        a = x / y

    except ZeroDivisionError:
        print("[ERROR]出现错误！无法中断程式！")
        print("错误类型： ZeroDivisionError: division by zero")
    except SyntaxError:
        print("[ERROR]出现错误！无法中断程式！")
        print("错误类型：语法错误！")
    except TypeError:
        print("[ERROR]出现错误！无法中断程式！")
        print("错误类型：类型错误！")
    else:
        print(a)
    finally:
        print("end")


# ============{诸城市}==================
fun1(int(input("数字1：")), int(input("数字2：")))
