# coding=utf-8
# encoding=utf-8
print("Copyright (c) 2010-2025 ComicPython6045 Communicate.\nAll Rights Reserved.\n")


def lesson(python):
    print(f'Hi,{python}')


# ========================================================
from lxml import etree

text = """
    <div>
        <ul>
            <li class="item-1"><a href="link1.html">first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link-5.html">fifth item</a></li>
        </ul>
    </div>  
    """
html = etree.HTML(text)
href_list = html.xpath('//li[@class="item-1"]/a/@href '
                       '| //li[@class="item-inactive"]/a/@href '
                       '| //li[@class="item-0"]/a/@href ')
title_list = html.xpath('//li[@class="item-1"]/a/text()'
                        '| //li[@class="item-inactive"]/a/text()'
                        '| //li[@class="item-0"]/a/text()'
                        )
li_list = html.xpath("//li[@class='item-1']")
# =====================================================
if __name__ == "__main__":
    print("直接打印")
    print(href_list)
    print(title_list)
if __name__ == "__main__":
    print("用字典打印 ")
    for href in href_list:
        item = {"href": href, "title": title_list[href_list.index(href)]}
        print(item)
if __name__ == "__main__":
    print("用if打印(只有//li[@class='item-1']的内容)")
    item1 = {}
    for li in li_list:
        if len(li.xpath("./a/@href")) > 0:
            item1["herf"] = li.xpath("./a/@href")[0]
        else:
            item1["href"] = None
        item1["title"] = li.xpath("./a/text()")[0] if len(li.xpath("./a/text()")) > 0 else None
        print(item1)
lesson("Python")
