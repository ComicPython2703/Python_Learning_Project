# coding=utf-8
# encoding=utf-8
if __name__ == '__main__':
    print("====================== RESTART:爬虫1.py =====================")
    print("已连接到 pydev 调试器(内部版本号 251.25410.159)")


# noinspection PyPep8Naming
def Copyright():
    print("\nCopyright (c) 2010-2025 ComicPython6045 Communicate.\nAll Rights Reserved.\n")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
# ==========={准备工作}==================
import requests
# =========={主程序}===================
url="https://www.baidu.com"
response=requests.get(url)
response.encoding = response.apparent_encoding
print("res码：",response)
print("响应体str类型：",response.text)
print("响应体bytes类体：",response.content)
print("状态码：",response.status_code)
print("响应头：",response.headers)
print("编码：",response.encoding)
print("Cookies：",response.cookies)
url1="https://cn.bing.com/th?id=OHR.PacificCrestTrail_ZH-CN9582395021_1920x1080.jpg"
response1=requests.get(url1)
with open("img1.jpg","wb") as f:
    f.write(response1.content)
