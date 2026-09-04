# coding=utf-8
"""
文件操作处理示例
"""
if __name__ == '__main__':
    print("====================== RESTART:文件操作处理.py =====================")
    print("已连接到 pydev 调试器(内部版本号 241.17011.127)")


def Copyright():
    print("\nCopyright (c) 2010-2024 ComicPython6405 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


Copyright()
print()

# =========={准备工作}==================
import random
import os

# ============{分隔符}==================
# ###############{创建函数或类}###################
list1 = ["单车欲问边\n", "属国过居延\n"]

# 确保"测试.txt"文件存在
if not os.path.exists("测试.txt"):
    # 如果文件不存在，创建文件并写入初始内容
    with open("测试.txt", "w", encoding="utf-8") as init_file:
        init_file.write("这是初始内容\n")

# 读取并显示原始内容
print("原始文件内容:")
with open("测试.txt", "r", encoding='utf-8') as file1:
    original_content = file1.read()
    print(original_content)
    print(f"文件名：{file1.name}, 访问模式：{file1.mode}")

print("2————————————")

# 修改文件内容
with open("测试.txt", "w+", encoding="utf-8") as file3:
    file3.writelines(list1)
    print("[WriteList][INFO]写入完成！")
    file3.seek(0)  # 将文件指针移回开头
    new_content = file3.read()
    print(f"修改后的文件内容：{new_content}")

print("3——————————————")

# 验证文件内容是否已更新
print("验证更新后的文件内容:")
with open("测试.txt", "r", encoding='utf-8') as file2:
    for i in range(3):  # 减少循环次数，避免过多输出
        file2.seek(0)  # 每次读取前重置文件指针
        lines = file2.readlines()
        print(f"读取{i}次: {lines}")

print("4——————————————————")

# 创建加法题目文件
print("生成加法题目...")
with open("加法.txt", "a+", encoding="utf-8") as file4:
    file4.write("\n下面是 100 道口算题：\n")
    for i in range(100):  # 生成100道题目
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        file4.write(f"{a}+{b}=\n")
    print("加法题目生成完成！")

print("程序执行完毕！")