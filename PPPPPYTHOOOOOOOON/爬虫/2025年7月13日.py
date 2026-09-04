# coding=utf-8
# encoding=utf-8
print("\nCopyright (c) 2010-2025 ComicPython6045 Communicate.\nAll Rights Reserved.\n")


def lesson(python):
    print(f'Hi,{python}')
# ==========={准备工作}==================
from lxml import etree
import requests

# ========={part 1}============

text = """
        <div>
            <ul>
                <li class="item-1"><a herf="link1.html">first item</a></li>
                <li class="item-2"><a herf="link2.html">second item</a> </li>
            </ul>
        </div>
"""
html1 = etree.HTML(text)
handeled_html_str = etree.tostring(html1, encoding='utf8').decode()
# ========{part 2}============================
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                  'Safari/537.36 Edg/108.0.1462.54'
            }

url = 'https://movie.douban.com/top250'
html2 = requests.get(url, headers=headers).content.decode('utf-8')
data = etree.HTML(html2)
movies = data.xpath('//span[@class="title"][1]/text()')
herfs = data.xpath('//div[@class="hd"]/a/@href')
scores = data.xpath('//span[@class="rating_num"]/text()')

# ==============================================
if __name__ == '__main__':
    print(type(html1))
    print(handeled_html_str)
if __name__ == '__main__':
    for i in range(len(movies)):
        print(f"电影：{movies[i]}  链接：{herfs[i]}评分：{scores[i]}")
